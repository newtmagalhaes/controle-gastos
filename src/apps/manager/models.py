from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # despesas: RelatedManager[CategoriaDespesa]
    # itens_despesas: RelatedManager[ItemDespesa]
    pass
