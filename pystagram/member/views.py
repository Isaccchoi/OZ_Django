from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import signing
from django.core.signing import SignatureExpired, TimestampSigner
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, FormView

from member.forms import LoginForm, SignupForm
from member.models import UserFollowing
from utils.email import send_email

User = get_user_model()


class SignupView(FormView):
    template_name = 'auth/signup.html'
    form_class = SignupForm
    # success_url = reverse_lazy('signup_done')

    def form_valid(self, form):
        user = form.save()
        # 이메일 발송
        signer = TimestampSigner()
        signed_user_email = signer.sign(user.email)
        signer_dump = signing.dumps(signed_user_email)

        # print(signer_dump)
        #
        # decoded_user_email = signing.loads(signer_dump)
        # print(decoded_user_email)
        # email = signer.unsign(decoded_user_email, max_age=60 * 30)
        # print(email)

        # http://localhost:8000/verify/?code=asdasdsa
        url = f'{self.request.scheme}://{self.request.META["HTTP_HOST"]}/verify/?code={signer_dump}'
        if settings.DEBUG:
            print(url)
        else:
            subject = '[Pystagram]이메일 인증을 완료해주세요'
            message = f'다음 링크를 클릭해주세요. <br><a href="{url}">{url}</a>'

            send_email(subject, message, user.email)

        return render(
            self.request,
            template_name='auth/signup_done.html',
            context={'user': user}
        )


def verify_email(request):
    code = request.GET.get('code', '')

    signer = TimestampSigner()
    try:
        decoded_user_email = signing.loads(code)
        email = signer.unsign(decoded_user_email, max_age=60 * 30)
    except (TypeError, SignatureExpired):
        return render(request, 'auth/not_verified.html')

    user = get_object_or_404(User, email=email, is_active=False)
    user.is_active = True
    user.save()
    return redirect(reverse('login'))
    # return render(request, 'auth/email_verified_done.html', {'user': user})


class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.user
        login(self.request, user)

        next_page = self.request.GET.get('next')
        if next_page:
            return HttpResponseRedirect(next_page)

        return HttpResponseRedirect(self.get_success_url())


class UserProfileView(DetailView):
    model = User
    template_name = 'profile/detail.html'
    slug_field = 'nickname'
    slug_url_kwarg = 'slug'
    queryset = User.objects.all()\
        .prefetch_related('post_set', 'post_set__images', 'following', 'followers')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            data['is_follow'] = UserFollowing.objects.filter(
                to_user=self.object,
                from_user=self.request.user
            )

        return data


class UserFollowingView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        pk = kwargs.get('pk', 0)
        to_user = get_object_or_404(User, pk=pk)

        if to_user == self.request.user:
            raise Http404

        # 만약 이미 팔로우가 되어있으면 팔로우 취소 => UserFollowing row 삭제
        # 안되어있으면 팔로우 시작 => UserFollowing row 생성
        following, created = UserFollowing.objects.get_or_create(
            to_user=to_user,
            from_user=self.request.user
        )

        if not created:
            following.delete()

        return HttpResponseRedirect(
            reverse('profile:detail', kwargs={'slug': to_user.nickname})
        )
