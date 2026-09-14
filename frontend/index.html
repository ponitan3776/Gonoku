<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>五目並べ | Gomoku</title>
<style>
  :root { --accent: #4f8cff; }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 24px 16px 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
    min-height: 100vh;
    background: radial-gradient(1200px 600px at 50% -10%, #26344d 0%, #10141d 60%, #0a0d13 100%);
    color: #e9eef8;
    font-family: "Hiragino Kaku Gothic ProN", "Yu Gothic UI", "Yu Gothic", Meiryo, system-ui, -apple-system, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  h1 { margin: 0; font-size: 1.35rem; letter-spacing: .28em; text-indent: .28em; font-weight: 700; }
  .subtitle { margin: -6px 0 0; font-size: .72rem; letter-spacing: .25em; color: #8ea0bd; }
  .panel { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center; }
  .field { display: flex; align-items: center; gap: 6px; font-size: .85rem; color: #a9b8d0; }
  select, button {
    font: inherit; font-size: .85rem; color: #e9eef8;
    background: #1b2433; border: 1px solid #33425c; border-radius: 9px;
    padding: 7px 12px; cursor: pointer;
    transition: background .15s, border-color .15s, transform .1s;
  }
  select:hover, button:hover { background: #24304a; border-color: #4a5f85; }
  button:active { transform: translateY(1px); }
  button.primary { background: var(--accent); border-color: var(--accent); color: #fff; font-weight: 600; }
  button.primary:hover { background: #6a9dff; border-color: #6a9dff; }
  select:disabled { opacity: .4; cursor: not-allowed; }
  #status { min-height: 1.6em; font-size: .95rem; text-align: center; letter-spacing: .04em; color: #cdd9ee; }
  #status.win  { color: #7ee08a; font-weight: 700; }
  #status.lose { color: #ff8b8b; font-weight: 700; }
  canvas {
    width: 100%; max-width: 600px; height: auto; display: block;
    border-radius: 12px; cursor: pointer;
    box-shadow: 0 18px 40px rgba(0,0,0,.55), 0 0 0 1px rgba(255,255,255,.06);
    touch-action: manipulation;
  }
  canvas.disabled { cursor: default; }
  .hint { margin: 0; font-size: .74rem; color: #7c8ba6; text-align: center; line-height: 1.7; }
  @media (max-width: 480px) { h1 { font-size: 1.1rem; } }
</style>
</head>
<body>
  <h1>五目並べ</h1>
  <p class="subtitle">GOMOKU</p>

  <div class="panel">
    <label class="field">モード
      <select id="mode">
        <option value="ai">vs コンピュータ</option>
        <option value="pvp">2人対戦</option>
      </select>
    </label>
    <label class="field">強さ
      <select id="difficulty">
        <option value="easy">やさしい</option>
        <option value="normal" selected>ふつう</option>
        <option value="hard">つよい</option>
      </select>
    </label>
    <button id="restart" class="primary">はじめから</button>
  </div>

  <div id="status"></div>
  <canvas id="board"></canvas>
  <p class="hint">交差点をクリック／タップして石を置きます。</p>

<script>
(function () {
  "use strict";

  var SIZE = 15;
  var EMPTY = 0, BLACK = 1, WHITE = 2;
  var PADDING = 20, CELL = 40;
  var BOARD_PX = PADDING * 2 + CELL * (SIZE - 1);  // 600
  var DPR = Math.max(1, Math.min(window.devicePixelRatio || 1, 3));

  var canvas = document.getElementById('board');
  var ctx = canvas.getContext('2d');
  canvas.width = BOARD_PX * DPR;
  canvas.height = BOARD_PX * DPR;

  var statusEl = document.getElementById('status');
  var modeEl = document.getElementById('mode');
  var diffEl = document.getElementById('difficulty');

  var state = {
    board: null,
    mode: 'ai',
    difficulty: 'normal',
    turn: BLACK,
    human: BLACK,
    ai: WHITE,
    over: false,
    winner: null,
    winLine: null,
    lastMove: null,
    thinking: false
  };

  function makeBoard() {
    var b = [];
    for (var y = 0; y < SIZE; y++) {
      var row = [];
      for (var x = 0; x < SIZE; x++) row.push(EMPTY);
      b.push(row);
    }
    return b;
  }

  function pos(i) { return PADDING + i * CELL; }

  /* ---------- 描画 ---------- */

  function drawStone(cx, cy, color) {
    var r = CELL * 0.42;

    // 影
    ctx.beginPath();
    ctx.arc(cx, cy + 2, r, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(40, 25, 5, 0.28)';
    ctx.fill();

    // 本体
    var g = ctx.createRadialGradient(cx - r * 0.35, cy - r * 0.4, r * 0.1, cx, cy, r * 1.05);
    if (color === BLACK) {
      g.addColorStop(0.0, '#7a8089');
      g.addColorStop(0.45, '#2b2f36');
      g.addColorStop(1.0, '#05070a');
    } else {
      g.addColorStop(0.0, '#ffffff');
      g.addColorStop(0.6, '#f2f4f7');
      g.addColorStop(1.0, '#c2c8d0');
    }
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.fillStyle = g;
    ctx.fill();

    ctx.lineWidth = 1;
    ctx.strokeStyle = (color === BLACK) ? 'rgba(0,0,0,.65)' : 'rgba(130,138,148,.75)';
    ctx.stroke();
  }

  function draw() {
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    ctx.clearRect(0, 0, BOARD_PX, BOARD_PX);

    // 盤面（木目）
    var g = ctx.createLinearGradient(0, 0, BOARD_PX, BOARD_PX);
    g.addColorStop(0.0, '#f2dcae');
    g.addColorStop(0.5, '#e8c98f');
    g.addColorStop(1.0, '#d9b273');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, BOARD_PX, BOARD_PX);

    // 外枠
    ctx.strokeStyle = 'rgba(122, 84, 32, .8)';
    ctx.lineWidth = 2;
    ctx.strokeRect(1, 1, BOARD_PX - 2, BOARD_PX - 2);

    // 格子
    ctx.strokeStyle = 'rgba(105, 72, 26, .72)';
    ctx.lineWidth = 1;
    for (var i = 0; i < SIZE; i++) {
      var p = pos(i);
      ctx.beginPath(); ctx.moveTo(pos(0), p); ctx.lineTo(pos(SIZE - 1), p); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(p, pos(0)); ctx.lineTo(p, pos(SIZE - 1)); ctx.stroke();
    }

    // 星
    var stars = [[3, 3], [11, 3], [3, 11], [11, 11], [7, 7]];
    ctx.fillStyle = 'rgba(80, 52, 16, .95)';
    for (var s = 0; s < stars.length; s++) {
      ctx.beginPath();
      ctx.arc(pos(stars[s][0]), pos(stars[s][1]), 3.6, 0, Math.PI * 2);
      ctx.fill();
    }

    // 石
    for (var y = 0; y < SIZE; y++) {
      for (var x = 0; x < SIZE; x++) {
        if (state.board[y][x] !== EMPTY) drawStone(pos(x), pos(y), state.board[y][x]);
      }
    }

    // 最終手のマーカー
    var lm = state.lastMove;
    if (lm && !state.winLine) {
      ctx.beginPath();
      ctx.arc(pos(lm.x), pos(lm.y), 4.5, 0, Math.PI * 2);
      ctx.fillStyle = '#ff4d4d';
      ctx.fill();
    }

    // 勝利ライン
    if (state.winLine && state.winLine.length >= 2) {
      var a = state.winLine[0];
      var b = state.winLine[state.winLine.length - 1];
      ctx.save();
      ctx.strokeStyle = 'rgba(255, 60, 60, .9)';
      ctx.lineWidth = 5;
      ctx.lineCap = 'round';
      ctx.beginPath();
      ctx.moveTo(pos(a[0]), pos(a[1]));
      ctx.lineTo(pos(b[0]), pos(b[1]));
      ctx.stroke();
      ctx.restore();
    }
  }

  /* ---------- 入力 ---------- */

  function toGrid(clientX, clientY) {
    var rect = canvas.getBoundingClientRect();
    if (!rect.width) return null;
    var scale = BOARD_PX / rect.width;
    var px = (clientX - rect.left) * scale;
    var py = (clientY - rect.top) * scale;
    var x = Math.round((px - PADDING) / CELL);
    var y = Math.round((py - PADDING) / CELL);
    if (x < 0 || x >= SIZE || y < 0 || y >= SIZE) return null;
    return { x: x, y: y };
  }

  function canPlay() {
    if (state.over || state.thinking) return false;
    if (state.mode === 'ai' && state.turn !== state.human) return false;
    return true;
  }

  canvas.addEventListener('click', function (e) {
    if (!canPlay()) return;
    var g = toGrid(e.clientX, e.clientY);
    if (!g) return;
    if (state.board[g.y][g.x] !== EMPTY) return;
    play(g.x, g.y);
  });

  /* ---------- 通信 ---------- */

  function delay(ms) {
    return new Promise(function (resolve) { setTimeout(resolve, ms); });
  }

  async function play(x, y) {
    var player = state.turn;
    state.thinking = true;
    updateStatus();

    var data;
    try {
      var tasks = [
        fetch('/api/move', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            board: state.board,
            x: x, y: y,
            player: player,
            mode: state.mode,
            difficulty: state.difficulty
          })
        })
      ];
      if (state.mode === 'ai') tasks.push(delay(220));

      var results = await Promise.all(tasks);
      var res = results[0];
      data = await res.json();
      if (!res.ok) throw new Error(data.error || 'サーバーエラー');
    } catch (err) {
      state.thinking = false;
      updateStatus();
      window.alert('エラー: ' + err.message);
      return;
    }

    state.board = data.board;
    state.lastMove = data.ai ? { x: data.ai.x, y: data.ai.y } : { x: x, y: y };

    if (data.win) {
      state.over = true;
      state.winner = data.win.player;
      state.winLine = (data.win.line && data.win.line.length) ? data.win.line : null;
    } else if (data.ai) {
      state.turn = state.human;
    } else {
      state.turn = (player === BLACK) ? WHITE : BLACK;
    }

    state.thinking = false;
    draw();
    updateStatus();
  }

  /* ---------- 表示更新 ---------- */

  function setStatus(text, cls) {
    statusEl.textContent = text;
    statusEl.className = cls || '';
  }

  function updateStatus() {
    canvas.className = canPlay() ? '' : 'disabled';

    if (state.over) {
      if (state.winner === 0) { setStatus('引き分けです'); return; }
      if (state.mode === 'ai') {
        if (state.winner === state.human) setStatus('🎉 あなたの勝ちです！', 'win');
        else setStatus('コンピュータの勝ちです', 'lose');
      } else {
        setStatus((state.winner === BLACK ? '黒' : '白') + 'の勝ちです！', 'win');
      }
      return;
    }
    if (state.thinking) { setStatus('コンピュータが考えています…'); return; }
    if (state.mode === 'ai') { setStatus('あなたの番です（● 黒）'); return; }
    setStatus(state.turn === BLACK ? '黒（●）の番です' : '白（○）の番です');
  }

  /* ---------- ゲーム管理 ---------- */

  function newGame() {
    state.board = makeBoard();
    state.mode = modeEl.value;
    state.difficulty = diffEl.value;
    state.turn = BLACK;
    state.human = BLACK;
    state.ai = WHITE;
    state.over = false;
    state.winner = null;
    state.winLine = null;
    state.lastMove = null;
    state.thinking = false;
    diffEl.disabled = (state.mode !== 'ai');
    draw();
    updateStatus();
  }

  document.getElementById('restart').addEventListener('click', newGame);
  modeEl.addEventListener('change', newGame);
  diffEl.addEventListener('change', function () {
    state.difficulty = diffEl.value;
  });

  newGame();
})();
</script>
</body>
</html>
