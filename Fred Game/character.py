


class Character():
    def __init__(self, health, speed, ammo):
        self.health = 5
        self.damage_dealt = 1
        self.speed = 1.00
        self.ammo = 0

    def get_health(self):
        return self.health
    
    def get_speed(self):
        return self.speed
    
    def get_ammo(self):
        return self.ammo
    
    def get_damage_dealt(self):
        return self.damage_dealt

    def set_health(self, hp):
        self.health = hp
    
    def set_speed(self, sp):
        self.speed = sp
    
    def set_damage_dealt(self, dps):
        self.damage_dealt = dps
        
    def set_ammo(self, ammo):
        self.ammo = ammo

class Player(Character):
    def__init__(self, health, speed, ammo):
    
    def death(self):
        print("YOU'RE DEAD!")
    
    def movement(self):
        return 0

class Enemy(Character):
    def__init__(self, health, speed, ammo):
    
    def respawn(self):
        print("I've come back from DEATH!")
    
    def player_tracking(self):
        print("I must find him! I must get VENGANCE!!")
