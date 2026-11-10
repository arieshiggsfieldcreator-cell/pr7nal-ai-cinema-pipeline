# Open-Source Timed Multi-Shot Cinematic Pipeline

A production-tested framework for generating multi-shot narrative scenes with strict spatial geometry, optical continuity, and frame-one locks.

## 📌 Core Architectural Principles

1. **First-Frame Occupancy Lock:** The opening shot must explicitly match the visual state of the previous frame. No establishing buffers or empty plates.
2. **Spatial Geometry Map:** Absolute physical measurements and hand/prop anchor tags prevent model-generated geometry shifts.
3. **Timed Cut Structure:** Internal hard cuts are explicitly timecoded with strict camera movement and focal length rules per beat.
4. **Lighting & Specularity Continuity:** Direct balance between primary directional light sources and localized specular glow elements.

---

## 🚀 Prompt Execution Structure

```text
SCENE CONTEXT
[Single unbroken narrative arc summary. Identifies active characters, immediate tension, and physical action.]

ACTIVE REFERENCES
[List of reference tags carrying identity, wardrobe, location geometry, and prop continuity.]

SCALE AND GEOMETRY
- Character Count: [Exact count]
- Distance & Staging: [Physical spacing in meters; anchor landmarks]
- Spatial Constraints: [Left/Right orientation locks; scanner/prop locations]

FORMAT & TIMING
- Mode: Timed Multi-Shot Sequence
- Cuts: Hard cuts at specified timestamps

TIME-CODED SHOT BREAKDOWN
 SHOT 1: [Camera Angle & Distance] | [Character Action] | [Prop Handoff / Focal Anchor]
 SHOT 2: [Medium Close / Reverse Angle] | [Event / Specular Activation / Reaction]
 SHOT 3: [Wide Horizon / Corridor Depth] | [Exit Motion / End State Alignment]

THE SCRIPT (Audio & Mouth Lock)
- Speaker: "[Verbatim line]"
- Non-speaking characters: HARD LOCK — mouths remain closed.

PHYSICS & MATERIAL BEHAVIOR
- Ground Friction: [Surface contact]
- Liquid & Particle Mechanics: [Viscosity, spray, parabolic arcs, surface residue]
- Mass & Inertia: [Weight shifts during handoffs]

LIGHTING & ATMOSPHERE
- Key Light: [Direction & Color Temperature]
- Secondary Light: [Ambient Fill]
- Emissive Light: [Localized UI / Specular glow]

AUDIO PROFILE
- Diegetic Sound: [Environmental ambient, footsteps, mechanical cues, foley]
- Music: None (Diegetic audio only)

LOCKS
- First frame matched to reference state.
- Zero position/side swapping across internal cuts.
- No burn-in UI or text overlays.
