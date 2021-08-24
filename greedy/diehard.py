#question : 
'''
The game is simple. You initially have ‘H’ amount of health and ‘A’ amount of armor. At any instant you can live in any of the three places - fire, water and air. After every unit time, you have to change your place of living. For example if you are currently living at fire, you can either step into water or air.

If you step into air, your health increases by 3 and your armor increases by 2

If you step into water, your health decreases by 5 and your armor decreases by 10

If you step into fire, your health decreases by 20 and your armor increases by 5

If your health or armor becomes <=0, you will die instantly

Find the maximum time you can survive.
'''


#approach : 
'''
->  The best approach is to live in air .. so for every odd time .. we live in air
->  Now we have to choose which one to go from air ..
->  IF health > 20 --> go to fire 
->  If health>5 and armour> 10 go to water 
->  If both are not possible ..GAME-OVER

'''

class Solution : 

    def livemax(self,health , armour ) : 

        def step_air (health , armour , time ):
            health += 3
            armour += 2 
            time  += 1 

        def step_fire(health , armour, time ):
            health -= 20
            armour += 5
            time += 1 

        def step_water(health , armour, time ):
            health -= 5
            armour -= 10
            time += 1 

        a = 1 
        f = 0
        w = 0
        time = 0
        health += 3 
        armour += 2 

        while health >0 and armour >0 :
            if f==1 : 
                step_air(health, armour , time)
                f = 0
                a = 1 
            elif w ==1 :
                step_air(health, armour , time )
                w = 0
                a = 1 
            elif a == 1 : 
                if health >20 : 
                    step_fire(health , armour , time )
                    f =1 
                    a = 0
                elif health > 5 and armour > 10 :
                    step_water(health , armour , time )
                    w = 1 
                    a = 0
                else : 
                    break

        return time 