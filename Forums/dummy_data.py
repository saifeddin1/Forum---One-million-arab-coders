from forums import models
from forums import stores

post_store = stores.PostStore()
post_store.add(models.Post("Life", "Life is alawys great"))
post_store.add(models.Post("Sunshine", "Sunshine is amazing"))
