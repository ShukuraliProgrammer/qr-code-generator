from django.contrib.auth.models import BaseUserManager


class UserManagar(BaseUserManager):
    def create_user(self, email, phone="", first_name="", last_name="", password=None):
        if not email:
            raise ValueError("Users must have an email.")
        
        user = self.model(
            email = self.normalize_email(email),
            phone=phone,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email = email,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



        