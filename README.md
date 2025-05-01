# 🦖 Dino Game RL

This project recreates the **Google Chrome Dinosaur Game** using **Pygame**, and then trains a Reinforcement Learning (RL) agent to play it using Deep Q-Learning (DQN).  
It’s a learning project for understanding both game development and RL from scratch.

---

## 📁 Project Structure

```
dino_game_rl/
│
├── game/              # Core game logic and objects (dino, obstacles, etc.)
│   ├── dino.py
│   ├── obstacle.py
│   ├── ground.py
│   ├── score.py
│   ├── game_env.py    # Gym-like interface for RL training
│   └── game_config.py
│
├── train/             # RL agent and training code
│   ├── dqn_agent.py
│   ├── train_dino.py
│   └── utils.py
│
├── assets/            # Game assets (images, sounds)
│   ├── DinoStart.png
│   ├── Cactus1.png
│   └── ...
│
├── main.py            # Play the game manually using keyboard
├── run_agent.py       # Let the trained RL agent play the game
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

## 🎮 How to Play the Game

### ▶️ Run the game manually
```bash
python main.py
```
- Press **Space** to make the dino jump.
- Avoid cacti and birds.
- Game ends on collision.

---

## 🧠 Reinforcement Learning

The RL agent (DQN-based) will:
- Observe the game state
- Choose actions (jump or do nothing)
- Receive rewards (e.g., +1 for surviving, -100 for crash)
- Learn to play better over time

You'll be able to train it with:
```bash
python train/train_dino.py
```

And run it with:
```bash
python run_agent.py
```

---

## 📦 Installation

### 1. Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/dino_game_rl.git
cd dino_game_rl
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📚 Requirements

- Python 3.7+
- pygame
- numpy
- torch or tensorflow (choose one for training)
- matplotlib

---

## 🙋‍♂️ Who is this for?

- Students learning **Pygame**
- Beginners curious about **Reinforcement Learning**
- Anyone who wants to see how a bot can learn to jump over cacti 😄

---

## 📝 Credits

- Game assets from: [https://github.com/harsitbaral/Dinosaur-Game](https://github.com/harsitbaral/Dinosaur-Game)
- Pygame + RL structure by Vo Tran Phi

---

## 🛠️ To Do

- [x] Implement base dino game
- [ ] Add flying obstacles
- [ ] Add game over screen
- [ ] Wrap game in `step()`/`reset()` interface
- [ ] Train RL agent (DQN)
- [ ] Record gameplay videos

---

## ⭐ Star this repo if you found it useful!