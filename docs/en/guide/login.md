# Sign in and sign out

Spatial Smart uses **Pinefield Single Sign-On (SSO)**. If you aren't signed in when you open the platform, you're redirected to the sign-in page at `alpha.pinefield.cn/pinefield.sso`.

<Shot src="/media/zh/login-sso.png" url="alpha.pinefield.cn/pinefield.sso" caption="Single sign-on (SSO) page: account, password, and a 6-digit captcha" />

## Sign in

::: steps
1. Enter your username in the **Account** (账号) field.
2. Enter your password in the **Password** (密码) field.
3. Click **Refresh** (换一个) next to the captcha image to get a new captcha.
4. **Immediately** type the 6 digits from the image into the **Captcha** (验证码) field.
5. Click **Sign in** (登 录). On success, you're returned to the Spatial Smart home screen.
:::

::: warning The captcha expires very quickly
The captcha becomes invalid after a few seconds — this is the most common reason sign-in fails. The right rhythm is: **fill in account and password → click Refresh → type the code right away → click Sign in right away**. If you get it wrong, click **Refresh** and try again, quickly.
:::

## If sign-in fails

When sign-in fails, the page shows a single message: **"User does not exist / wrong password / wrong captcha"** (用户不存在/密码错误/验证码错误). It doesn't tell you which one is wrong. Check in this order:

| Order | What to check | How |
| --- | --- | --- |
| 1 | Captcha expired or misread | Click **Refresh**, read it carefully, then enter it and sign in immediately |
| 2 | Password case | Make sure Caps Lock is off — passwords are case-sensitive |
| 3 | Account name | Account names are case-sensitive; watch out for extra spaces |
| 4 | Account access | Ask your administrator to confirm your account has Spatial Smart enabled |

## Sign out

::: steps
1. Click your avatar in the bottom-left corner (it shows your username).
2. In the **Personal** (个人) menu, click the red **Sign out** (退出登录).
:::

<Shot src="/media/zh/shell-user-menu.png" caption="Personal menu: Settings, Monthly usage, Feedback, Sign out" marks="10,92,1" />
