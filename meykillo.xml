<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Rifa</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    .container {
      max-width: 800px;
      margin: 20px auto;
      padding: 0 20px;
    }

    h1 {
      text-align: center;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-group label {
      display: block;
      font-weight: bold;
    }

    .form-group input[type="text"] {
      width: 100%;
      padding: 5px;
    }

    .form-group select {
      width: 100%;
      padding: 5px;
    }

    .form-group button {
      background-color: #333;
      color: #fff;
      border: none;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }

    .raffle-results {
      margin-top: 40px;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Rifa</h1>
    <div class="form-group">
      <label for="name">Nome:</label>
      <input type="text" id="name" name="name" placeholder="Digite seu nome">
    </div>
    <div class="form-group">
      <label for="number">Número:</label>
      <input type="int" id="number" name="number" placeholder="Digite um número">
    </div>
    <div class="form-group">
      <button onclick="submitRaffleEntry()">Participar da Rifa</button>
    </div>
    <div class="form-group">
      <button onclick="drawWinner()">Sortear Vencedor</button>
    </div>
    <div class="raffle-results" id="raffleResults"></div>
  </div>

  <script>
    var entries = [];

    function submitRaffleEntry() {
      var name = document.getElementById("name").value;
      var number = document.getElementById("number").value;
      var raffleResults = document.getElementById("raffleResults");

      if (!name || !number) {
        raffleResults.innerHTML = "Por favor, preencha todos os campos.";
        return;
      }

      if (entries[number]) {
        raffleResults.innerHTML = "O número selecionado já foi escolhido. Por favor, escolha outro.";
        return;
      }

      entries[number] = name;
      raffleResults.innerHTML = "O participante " + name + " escolheu o número " + number + ".";
    }

    function drawWinner() {
      var raffleResults = document.getElementById("raffleResults");
      var participantCount = Object.keys(entries).length;

      if (participantCount === 0) {
        raffleResults.innerHTML = "Não há participantes na rifa.";
        return;
      }

      var randomIndex = Math.floor(Math.random() * participantCount);
      var winningNumber = Object.keys(entries)[randomIndex];
      var winner = entries[winningNumber];

      raffleResults.innerHTML = "O número sorteado é " + winningNumber + ", e o vencedor é " + winner + ".";
    }
  </script>
</body>
</html>
