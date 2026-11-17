# Chimp Office — Visual Interface Concept

**Project:** Trader Joe's Agent  
**Proposed technology:** Phaser 4 (JavaScript game framework)  
**Status:** Concept and early project setup; the interactive office has **not** been implemented or validated.  
**Relationship to Trader Joe's:** Optional presentation interface for the private Python agent; not the trading engine itself.

## The idea in one sentence

Imagine opening Trader Joe's Agent and seeing a small animated office staffed by cartoon chimps: instead of reading a wall of terminal messages, you watch a friendly, game-like workspace that **illustrates** what the software is doing at a high level.

The characters are a visual metaphor for software activities. They are not separate AI traders or independently authorized decision-makers. The Python application remains responsible for actual analysis, safety decisions, and any permitted operations; the office would merely portray **approved, non-sensitive status information**.

## Picture the room

The proposed scene is a cozy, slightly chaotic, top-down or angled 2D office. There are desks with glowing monitors, a central board showing a few high-level statuses, filing cabinets, a coffee area, and tiny chimps moving between stations. When the app is idle, the room feels calm: screens pulse softly, someone sips coffee, and the status board says that nothing is underway. When an approved status event arrives, a chimp gets up and walks to the corresponding workstation.

A conceptual layout (not a screenshot or implemented game map):

```text
+------------------------------------------------------------------+
|                  TRADER JOE'S — CHIMP OFFICE                     |
|                                                                  |
|  [Market Desk]      [Analysis Desk]       [Safety Desk]          |
|    Chimp A             Chimp B              Chimp C              |
|    monitor             charts              checklist            |
|                                                                  |
|                    [CENTRAL STATUS BOARD]                        |
|                Observation | Review | Paused                     |
|                                                                  |
|  [Records Desk]      [Visitor/Review Desk]    [Coffee Corner]     |
|    Chimp D                Chimp E               idle chimps       |
|    filing cabinet        approval bell                           |
|                                                                  |
+------------------------------------------------------------------+
```

The stations are **storytelling choices**, not a disclosure of the private application's modules, execution order, dependencies, or internal architecture.

## What a viewer might see

### Scene 1 — Quiet morning

The office opens with warm desk lamps and a small sign that reads **Observation Mode**. The chimps are at their stations. No one is placing an order. The main status panel makes it clear that the interface is educational and that observing activity is different from approving or executing anything.

### Scene 2 — Market information arrives

A monitor lights up at the market desk. Its chimp adjusts glasses and studies a stylized chart, while a small notification appears: **New market information reviewed**. There are no real ticker lists, scan schedules, data-source details, or strategy settings displayed.

### Scene 3 — Analytical review

Another chimp walks to a desk with paper charts and colorful shapes. The board changes to **Analysis in progress**. A simple animation communicates work being performed, without revealing indicator values, proprietary combinations, ranking systems, or trading decisions.

### Scene 4 — Safety review

At a separate desk, a chimp inspects a cartoon checklist. The viewer might see **Review required**, **Check passed**, or **Action blocked**. This is deliberately a high-level status display, not a copy of real risk rules, limits, or internal decision logic. A blocked status might appear as a red STOP stamp and a paused animation rather than a detailed error message.

### Scene 5 — Human supervision

A bell rings near the review desk. A chimp points to a visible sign: **Waiting for operator**. The interface communicates that the real software may require deliberate user involvement; it does **not** grant authority itself or bypass any control. An illustration of approval must never be treated as actual broker authorization.

### Scene 6 — Logging and recovery

At the records desk, a chimp files a document after a *sanitized* status update. If a simulated interruption occurs, the lights briefly flicker, then the room switches to **Paused — verification required**. This demonstrates the importance of reliability in a way a nontechnical audience can understand. The animation does not assert that an unresolved real condition has been recovered.

## Example animated sequences (proposed)

| High-level event | Office animation | What it communicates |
| --- | --- | --- |
| Application idle | Chimps sit, drink coffee, or glance at monitors | No active demonstration task |
| Market observation | Market-desk monitor lights up | Information is being examined |
| Analysis underway | A chimp studies a chart | General analytical activity |
| Safeguard blocks an action | STOP sign appears; chimp returns to desk | A protective condition prevented progression |
| Operator input needed | Review bell lights up | Human attention is required |
| Uncertain state | Characters freeze; status board shows PAUSED | Uncertainty should be visible, not silently treated as success |
| Sanitized event recorded | Records chimp files a paper | A demonstration event has been logged |

These are **potential UI animations**, not demonstrations of implemented event integration.

## The user experience

The intended experience is to make advanced software easier to understand and more enjoyable to observe. A first-time visitor could understand the basic idea in seconds: the chimps represent tasks; desks represent broad types of work; the big board shows whether the system is observing, reviewing, blocked, or waiting. A technical viewer could switch to a text-only or accessible event summary for precise descriptions.

The office could also include a **Demo Mode**, driven by manually scripted and completely fictional events, so the animation can be shown during a class presentation without connecting to any market account or private internal logs.

## Technology concept: Phaser 4

Phaser is a JavaScript framework for building browser-based 2D interactive scenes. It is an appropriate candidate for animated sprites, room layouts, simple character movement, text panels, and transitions. A future implementation could use original or appropriately licensed art assets.

**Verified current setup:** The private development repository contains a `chimp-office` npm package with a Phaser 4 dependency. At the last review, that package did **not** contain a committed playable scene, characters, or operational connection to the Python agent. The scene described here remains proposed work.

A safe early prototype would run on synthetic status events only. Any later integration would require its own access-control, data-minimization, and reliability review. The graphical scene must remain informational: it must not be an alternate path around safety checks or a mechanism to submit orders.

## Development milestones

- [x] Discuss the animated-office idea as a future presentation concept.
- [x] Create the initial Phaser 4 npm project setup in private development.
- [x] Document a detailed public-facing concept without exposing private code.
- [ ] Build a basic office scene with original placeholder art and an idle animation.
- [ ] Add animated chimps and distinct desk interactions using fictional events.
- [ ] Add a readable on-screen status board and accessible text equivalent.
- [ ] Demonstrate paused and blocked states in a fully offline scenario.
- [ ] Evaluate whether connecting sanitized, read-only application events is appropriate.
- [ ] Prepare a supervised classroom demonstration if the feature becomes ready.

## What this concept intentionally does not expose

This document does not specify any actual scan timing or universe, indicators as configured in the agent, risk thresholds, order-submission internals, broker payloads, API keys, private event schema, or system dependency graph. The room layout and sequence above exist solely to help readers imagine a **future visualization**, not to diagram how the private trading application works.

## Why include it in the coursework portfolio?

It gives the project a potential human-centered interface component that complements the current engineering emphasis on testing and reliability. It also offers a way to explain the software to nontechnical classmates or an instructor without publishing proprietary implementation details. **The real private trading agent remains the primary semester project; the Chimp Office is an optional extension.**
