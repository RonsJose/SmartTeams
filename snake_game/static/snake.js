const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

const box = 20;  
let snake = [];
let food = {};
let direction = "RIGHT";
let gameInterval = null;
let score = 0;

function initGame() {
    snake = [{ x: 9 * box, y: 9 * box }];
    food = { x: Math.floor(Math.random() * 20) * box, y: Math.floor(Math.random() * 20) * box };
    direction = "RIGHT";
    score = 0;

    // Update score display
    document.getElementById("scoreDisplay").innerText = "Score: " + score;

    if (gameInterval) clearInterval(gameInterval);

    const controls = document.getElementById("gameControls");
    controls.innerHTML = "";

    gameInterval = setInterval(drawGame, 100);
}

document.addEventListener("keydown", function(event) {
    // Prevent arrow keys from scrolling the page
    if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].includes(event.key)) {
        event.preventDefault();
    }

    if (event.key === "ArrowLeft" && direction !== "RIGHT") direction = "LEFT";
    if (event.key === "ArrowRight" && direction !== "LEFT") direction = "RIGHT";
    if (event.key === "ArrowUp" && direction !== "DOWN") direction = "UP";
    if (event.key === "ArrowDown" && direction !== "UP") direction = "DOWN";
});


function drawGame() {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, 400, 400);

    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = i === 0 ? "lime" : "green";
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }

    ctx.fillStyle = "red";
    ctx.fillRect(food.x, food.y, box, box);

    let head = { ...snake[0] };
    if (direction === "LEFT") head.x -= box;
    if (direction === "RIGHT") head.x += box;
    if (direction === "UP") head.y -= box;
    if (direction === "DOWN") head.y += box;

    if (head.x < 0 || head.y < 0 || head.x >= 400 || head.y >= 400 || collision(head)) {
        clearInterval(gameInterval);
        showGameOver();
        return;
    }

    if (head.x === food.x && head.y === food.y) {
        // Eat food
        score++;
        document.getElementById("scoreDisplay").innerText = "Score: " + score;
        food = { x: Math.floor(Math.random() * 20) * box, y: Math.floor(Math.random() * 20) * box };
    } else {
        snake.pop();
    }

    snake.unshift(head);
}

function collision(head) {
    for (let segment of snake) {
        if (head.x === segment.x && head.y === segment.y) return true;
    }
    return false;
}

function showGameOver() {
    ctx.fillStyle = "white";
    ctx.font = "30px Arial";
    ctx.fillText("Game Over!", 110, 200);

    const controls = document.getElementById("gameControls");
    controls.innerHTML = "";

    const btn = document.createElement("button");
    btn.innerText = "Restart";
    btn.style.padding = "10px 20px";
    btn.style.fontSize = "18px";

    controls.appendChild(btn);
    btn.addEventListener("click", initGame);
}

// Start the game
initGame();



