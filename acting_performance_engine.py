"""
Acting & Performance Engine (Open AI Cinema Tools)
Generates structured behavioral prompt blocks for AI video engines,
focusing on physical actions, eye-life saccades, and tension states.
"""

class PerformanceEngine:
    def __init__(self, character_name: str, baseline_engine: str):
        self.character_name = character_name
        self.baseline_engine = baseline_engine

    def build_acting_block(
        self, 
        dialogue_delivery: str, 
        reaction_state: str, 
        eye_behavior: str, 
        physical_business: str
    ) -> str:
        """
        Compiles behavioral parameters into observable physical acting prompts.
        """
        acting_block = (
            f"ACTING ({self.character_name.upper()}):\n"
            f"- Verbal Delivery: {dialogue_delivery}\n"
            f"- Emotional Engine: Played through physical behavior under pressure, not facial mugging.\n"
            f"- Eye Life: {eye_behavior} Eyes lead the thought before head movement.\n"
            f"- Reaction & Business: {reaction_state} Physical task: {physical_business}.\n"
            f"- Micro-Behavior: Natural blink rate; breath dynamics match physical output."
        )
        return acting_block

if __name__ == "__main__":
    # Example generation for sci-fi narrative character
    engine = PerformanceEngine("Kai", "Suppressed Emotion Under Pressure")
    prompt_output = engine.build_acting_block(
        dialogue_delivery="Flat, economical, quiet delivery. No shouting.",
        reaction_state="Freezes momentarily upon reading data; shock expressed strictly in eyes.",
        eye_behavior="Micro-saccades scanning display dots; rapid focus shift.",
        physical_business="Holding liquid cup, executing sudden spit-take, head jerking back slightly."
    )
    print(prompt_output)
