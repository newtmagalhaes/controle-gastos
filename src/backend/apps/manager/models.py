from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # despesas: RelatedManager[CategoriaDespesa]
    # itens_despesas: RelatedManager[ItemDespesa]
    pass
