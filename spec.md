# Turtle Crossing Game - Developer Specification

## Overview
A simple **Turtle Crossing** game using Python's `turtle` library. The player controls a turtle that must cross the screen from bottom to top while avoiding moving cars. Each successful crossing increases the score and game difficulty.

## Game Mechanics

### Objective
- The player moves a turtle from the **bottom** to the **top** of the screen.  
- The goal is to **reach the top row** while avoiding **moving cars**.  
- When the turtle reaches the top, the **score increases by 1**, the turtle resets, and the **game speed increases**.  
- If the turtle collides with a car, the **game is over** and the screen freezes.

### Movement & Controls
- The player uses **arrow keys** to move the turtle.
- The turtle moves **step-by-step**, **30 pixels per move** (both horizontally and vertically).

### Screen & Layout
- **Fixed size:** `600x600` pixels.
- The screen consists of **20 rows** (`30px` each).
  - The **bottom** and **top rows** are **safe zones**.
  - The **middle 18 rows** contain moving cars.

### Cars & Traffic
- Cars **move from right to left** only.
- Car speeds are categorized by color:
  - **Red cars** → **Fastest**
  - **Green cars** → **Slowest**
  - **Other cars (random colors except red/green)** → **Normal speed**
- Cars **spawn randomly** but always leave a **minimum gap** in the same lane.
- Cars **despawn** after exiting the left side of the screen.
- Cars spawn at random intervals but **must allow passage opportunities**.  

### Difficulty Scaling
- **After each successful crossing:**
  - The **car speed increases**.
  - The **spawn rate may increase** (configurable variable).

### Visuals
- **Background:** Solid white.
- **Turtle:** Black (default turtle shape from `turtle` library).
- **Cars:** Simple **rectangles** (random colors except for red/green).

### Scoring & Game Over
- **Score is displayed in the top-left corner.**
- **Game Over triggers:** When the turtle collides with a car.
- **On Game Over:**
  - The screen **freezes**.
  - A **"Game Over"** message appears with the final score.

## Architecture & Implementation

### Main Components
| Component       | Description |
|----------------|-------------|
| `Turtle` (Player) | A turtle object controlled by arrow keys. Moves 30px per step. |
| `Cars` (Obstacles) | Rectangular shapes that move from right to left at variable speeds. |
| `Game Manager` | Handles game state, score, difficulty scaling, and collision detection. |
| `Spawner` | Controls car generation and ensures gaps between vehicles. |

### Data Handling & Configurations  

## Error Handling Strategies
- **Boundary checks:** Prevents the turtle from moving outside the screen.  
- **Collision detection:** Ensures the game ends when the turtle **touches** a car.  
- **Spawn validation:** Ensures there’s always a **gap** for the player to pass.  

## Future Enhancements (Optional)
- **Restart function** (e.g., press `R` to restart after Game Over).
- **Custom car sprites** using `.gif` images.
- **Sound effects** for movement and collisions.
- **Dynamic background (road, lane markings, etc.)**.