class Skill:
    def __init__(self, skill_type, mana_cost, dmg, stun):
        self.skill_type = skill_type
        self.mana_cost = mana_cost
 
        self.__dmg = dmg
        self.__stun = stun
 
    def get_damage(self):
        return self.__dmg
 
    def level_up(self, amount):
        if amount > 0:
            self.__dmg += amount
        else:
            print(f"Invalid level up amount: {amount}. Damage unchanged.")
 
    def use(self):
        stun_text = "and stuns the enemy" if self.__stun else "with no stun effect"
        return (f"{self.skill_type} skill used for {self.mana_cost} mana, "
                f"dealing {self.__dmg} damage {stun_text}.")
 
    def show_status(self):
        return (f"Type: {self.skill_type} | Mana Cost: {self.mana_cost} | "
                f"Damage: {self.__dmg} | Stun: {self.__stun}")
 
 
class Character:
    def __init__(self, name, hp):
        self.name = name
 
        self.__hp = hp
 
        self.skills = []
 
    def learn_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.name} learned {skill.skill_type}!")
 
    def use_skill(self, skill_type):
        for skill in self.skills:
            if skill.skill_type == skill_type:
                print(f"{self.name} casts {skill_type}!")
                print(skill.use())
                return
        print(f"{self.name} does not know {skill_type}.")
 
    def list_skills(self):
        return [skill.skill_type for skill in self.skills]
 
    def show_status(self):
        return f"Name: {self.name} | HP: {self.__hp} | Skills known: {len(self.skills)}"
 
 
if __name__ == "__main__":
    aria = Character(name="Aria", hp=100)
 
    fireball = Skill(skill_type="Fireball", mana_cost=20, dmg=35, stun=False)
    iceshard = Skill(skill_type="Ice Shard", mana_cost=15, dmg=20, stun=True)
    heal = Skill(skill_type="Heal", mana_cost=10, dmg=0, stun=False)
 
    print("--- BEFORE RELATIONSHIP ---")
    print(aria.show_status())
    print("Skills created independently:", fireball.skill_type, "|", iceshard.skill_type, "|", heal.skill_type)
 
    print("\n--- BUILDING RELATIONSHIP ---")
    aria.learn_skill(fireball)
    aria.learn_skill(iceshard)
    aria.learn_skill(heal)
 
    print("\n--- AFTER RELATIONSHIP ---")
    print(aria.show_status())
    print("Related object(s) - Aria's known skills:", aria.list_skills())
 
    print("\nUsing skills through the relationship:")
    for skill in aria.skills:
        print(" -", skill.use())
 
    print("\nCalling a specific skill by name through Character.use_skill():")
    aria.use_skill("Fireball")
