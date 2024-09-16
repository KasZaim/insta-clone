from instadb.models import Comments, UserProfile, Posts,Likes

user1 = UserProfile.objects.create(username="JasminTasty", profile_image="img/Profilbilder/ali-pazani-2613260.jpg")
user2 = UserProfile.objects.create(username="Fashion Nova", profile_image="img/Profilbilder/daniel-xavier-1239288.jpg")
user3 = UserProfile.objects.create(username="Healthy_recipes", profile_image="img/Profilbilder/pixabay-38554.jpg")
user4 = UserProfile.objects.create(username="Travel_addicted", profile_image="img/Profilbilder/pexels-pixabay-413959.jpg")

post1 = Posts.objects.create(user_profile=user1, description="Das Rezept für die Pancakes gibt es in meiner Bio :-)", image="img/posts/img1.jpg", description_headline="Breakfast for Champions,",hashtags="#foodie #lazy")
post2 = Posts.objects.create(user_profile=user2, description="Leute checkt die neue Kollektion von Prana Luna for Her ab! Die haben ein paar richtig nice Outfits für euch", image="'img/posts/img2.jpg', 'img/posts/img3.jpg', 'img/posts/img4.jpg'", description_headline="Photoshoot for the New Brand Prana Luna.",hashtags="#fashion #instalife #prana")
post3 = Posts.objects.create(user_profile=user3, description="mit unglaublichen 50gr Protein pro Portion, und dazu schmeckt es einfach fantastisch", image="img/posts/img5.jpg", description_headline="Hier haben wir ein High Protein Porridge,",hashtags="#goodlife #healthylifestyle #fruits")
post4 = Posts.objects.create(user_profile=user4, description="diesesmal bin ich in Budapest.. und was soll ich sagen es ist einfach schön hier zu der Jahreszeit!", image="img/posts/img6.jpg", description_headline="Mal wieder unterwegs,",hashtags="#travel #vloglifestyle #happy")


comments1 = Comments.objects.create(post=post1, user_profile=user1, comment_text="Yummy")
comments2 = Comments.objects.create(post=post1, user_profile=user2,comment_text="Das sieht Lecker aus!")
comments3 = Comments.objects.create(post=post2, user_profile=user2,comment_text="Slayin that Outfit")
comments4 = Comments.objects.create(post=post2, user_profile=user2,comment_text="Nice")
comments5 = Comments.objects.create(post=post3, user_profile=user2,comment_text="Perfekt für den Muskelaufbau !")
comments6 = Comments.objects.create(post=post3, user_profile=user2,comment_text="need the recipe..")
comments7 = Comments.objects.create(post=post4, user_profile=user2,comment_text="#Travel")
comments8 = Comments.objects.create(post=post4, user_profile=user2,comment_text="Nice")


# order1 = Order.objects.create(customer=customer1, bill=bill1)
# order2 = Order.objects.create(customer=customer2, bill=bill2)
# order3 = Order.objects.create(customer=customer3, bill=bill3)
# order4 = Order.objects.create(customer=customer3, bill=bill4)
# order5 = Order.objects.create(customer=customer3, bill=bill5)

# Producttype.objects.create(order=order1, product=product1, type_name="Wood")
# Producttype.objects.create(order=order1, product=product2, type_name="Iron")

# Producttype.objects.create(order=order2, product=product1, type_name="Wood")
# Producttype.objects.create(order=order2, product=product3, type_name="Plastic")

# Producttype.objects.create(order=order3, product=product1, type_name="Wood")
# Producttype.objects.create(order=order3, product=product2, type_name="Iron")
# Producttype.objects.create(order=order3, product=product3, type_name="Plastic")


# delete all


UserProfile.objects.all().delete()
Posts.objects.all().delete()
Comments.objects.all().delete()