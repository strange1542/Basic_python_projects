# adventure game 

print("Welcome to the MCU")

var1 = input("Hello player welcome to the MCU world if you want to go on titan press /t/ or if you want to fight thanos on the earth then press /e/ :").lower()
if var1 == "t":
    var2 = input("Hello player now you are iron man you had foght with the childerns of thanos and they defeated you and took the Dr. to their ship now you are going to titan with spider kid press /h/ to send the kid back to home or press /c/ to call pepper and tell her that you'll gonna late for dinner :").lower()
    if var2 == "h":
        print("the spider kid was suppose to go home but he stick with the ship and he is now with you and foght with you and at the end he got vanished.")
    elif var2 == "c":
        print("You called pepper but there was poor connection so you don't get to talk with her and now you are going to titan to save the one with time stone you met with gardians and they timeup with you and you'll fight greatly but lost the stone.")
    else: 
        print("Please enter a valid caracter.")
elif var1 == "e":
    var3 = input("Hello there now you are captain america and you were hiding in the shadow until the world needs you and now is the time to fight for world to save the loved once. Proxima midnight and corvus glaive fight with captain, natasha & wanda and they lost and ran away now press /h/ to go home or press /w/ to go wakanda :").lower()
    if var3 == "h":
        print("You are going back to home and you met with roudy and Dr.banner and then you all met with each ohter after very long time and now you have to save vision so you with all members going to wakanda.")
    elif var3 == "w":
        print("With rest of the team you are now going to wakanda to save vision after reaching their the wakandain are now preparing to fight with thanos they foght greatly but in they and the heros lost the fight and thanos snaped his finger and he did what he said he vanished half of the universe and then he open a portal and vanishes from planet earth.")
    else:
        print("Please enter a valid caracter.")

print("the end is the beginning")
