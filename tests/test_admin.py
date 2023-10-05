from firelit.admin import FirebaseAdmin
from firelit.utils import load_yaml


def test_admin():
    """Test admin module"""
    configurations = [
        dict(
            email="user@gmail.com",
            password="firelit",
        ),
        dict(
            email="alex@gmail.com",
            password="laurea",
        )
    ]

    admin = FirebaseAdmin("firelit_config.yml")
    admin.login(configurations[0]["email"], configurations[0]["password"])
    assert admin.authentication_status, ("This user should be "
                                         "authenticated")

    admin.reset_connection()
    admin.login(configurations[1]["email"], configurations[1]["password"])
    assert not admin.authentication_status, ("This user should not be "
                                             "authenticated")

    # Testing load from dictionary
    config = load_yaml("firelit_config.yml")
    admin = FirebaseAdmin(config)
    admin.login(configurations[0]["email"], configurations[0]["password"])
    assert admin.authentication_status, "This user should be authenticated"

    # Testing from local file
    admin = FirebaseAdmin()
    admin.login(configurations[0]["email"], configurations[0]["password"])
    assert admin.authentication_status, "This user should be authenticated"

