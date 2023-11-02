from pweb import Blueprint , flash
from pweb_form_rest import ssr_ui_render
from boot.form.member_form import MemberForm

url_prefix = "/"
auth_controller = Blueprint(
    "auth_controller",
    __name__,
    url_prefix=url_prefix
)

@auth_controller.route("/", methods=['GET'])

@auth_controller.route("/login", methods=['GET', 'POST'])
def login():
    form = MemberForm()
    if form.is_valid_data_submit():
        flash("Valid data submitted", "success")
    return ssr_ui_render(view_name="member/login", form=form)


@auth_controller.route("/registration", methods=['GET', 'POST'])
def registration():
    form = MemberForm()
    if form.is_valid_data_submit():
        flash("Valid data submitted", "success")
    return ssr_ui_render(view_name="member/registration", form=form)
