class PotionGenerator:
    #c 1.13 по 1.19.4+
    
    def _get_effect_id(self, effect_name):
        effect_ids = {
            "speed" : 1,
            "slowness" : 2,
            "haste" : 3,
            "mining fatigue" : 4,
            "strength" : 5,
            "instant health" : 6,
            "instant damage" : 7,
            "jump boost" : 8,
            "nausea" : 9,
            "regeneration" : 10,
            "resistance" : 11,
            "fire resistance" : 12,
            "water breathing" : 13,
            "invisibility" : 14,
            "blindness" : 15,
            "night vision" : 16,
            "hunger" : 17,
            "weakness" : 18,
            "poison" : 19,
            "wither" : 20,
            "health boost" : 21,
            "absorption" : 22,
            "saturation" : 23,
            "glowing" : 24,
            "levitation" : 25,
            "luck" : 26,
            "bad luck" : 27,
            "slow falling" : 28,
            "conduit power" : 29,
            "dolphin's grace" : 30,
            "bad omen" : 31,
            "hero of the village" : 32,
            "darkness" : 33
        }
        effect_id = effect_ids.get(effect_name)
        if effect_id is None: 
            raise ValueError(f"Unknown effect: {effect_name}")
        return effect_id
    
    def _generate_effects_string(self, effects:list[dict], no_particle:bool):
        effects_list = []
        for effect in effects:
            effect_name = effect.get("effect_name", "")
            level = effect.get("effect_level", 1)
            duration = effect.get("effect_duration", None)
            
            if duration is not None and duration < -1:
                raise ValueError(f"Duration cant be less than -1, yours is {duration}")
                
            if level < 1 or level > 128:
                raise ValueError(f"Effect level should be from 1 to 128, yours is: {level}")
            
            effect_id = self._get_effect_id(effect_name)
            duration_ticks = duration * 20 if duration is not None else -1
            if no_particle:
                effect_str = f"{{Id:{effect_id},Amplifier:{level-1},Duration:{duration_ticks},ShowParticles:0b}}"
            else:
                effect_str = f"{{Id:{effect_id},Amplifier:{level-1},Duration:{duration_ticks}}}"
            effects_list.append(effect_str)
        return "CustomPotionEffects:[" + ",".join(effects_list) + "]"
        
        
    def generate_command(self, type:str, effects:list[dict], no_particle:bool=False, potion_name:str="", description:str=""):
        type_strings = {
            "potion_regular":"/give @p minecraft:potion{Potion:\"minecraft:water\",",
            "potion_splash":"/give @p minecraft:splash_potion{Potion:\"minecraft:water\",",
            "potion_lingering":"/give @p minecraft:lingering_potion{Potion:\"minecraft:water\",",
            "potion_arrow":"/give @p minecraft:tipped_arrow{Potion:\"minecraft:water\","
        }
        
        potion_type = type_strings.get(type)
        potion_effects = self._generate_effects_string(effects, no_particle)
        if potion_name == "":
            potion_lore = "}"
        else:
            potion_lore = f',display:{{Name:"\\"{potion_name}\\"",Lore:["\\"{description}\\""]}}}}'
        
        return potion_type + potion_effects + potion_lore