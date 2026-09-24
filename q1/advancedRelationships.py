from classRelationships import Skill, Character


class CombatSkill(Skill):
    def __init__(self, skill_type, mana_cost, dmg, stun, range_type):
        super().__init__(skill_type, mana_cost, dmg, stun)
        self.range_type = range_type

    def show_range(self):
        return f"{self.skill_type} is a {self.range_type}-range combat skill."


if __name__ == "__main__":
    print("--- TEST 1: INHERITANCE ---")

    fireball = CombatSkill(
        skill_type="Fireball",
        mana_cost=20,
        dmg=35,
        stun=False,
        range_type="long"
    )

    print("Skill type:", fireball.skill_type)
    print("Mana cost:", fireball.mana_cost)
    print("Damage:", fireball.get_damage())
    print(fireball.show_range())
    print(fireball.use())

    print("\n--- TEST 2: AGGREGATION ---")

    aria = Character(name="Aria", hp=100)

    iceshard = Skill(
        skill_type="Ice Shard",
        mana_cost=15,
        dmg=20,
        stun=True
    )

    heal = Skill(
        skill_type="Heal",
        mana_cost=10,
        dmg=0,
        stun=False
    )

    print("Skills were created independently.")
    print("Before learning:", aria.list_skills())

    aria.learn_skill(fireball)
    aria.learn_skill(iceshard)
    aria.learn_skill(heal)

    print("After learning:", aria.list_skills())
    print("Character:", aria.name)
    print("Skills:", aria.list_skills())

    print("\n--- TEST 3: INHERITED METHOD ---")

    fireball.level_up(10)
    print("Fireball damage after level up:", fireball.get_damage())