const input = require('readline-sync');

console.log('Boas vindas! Tente adivinhar o número secreto (1 a 10)');

const numeroSecreto = 5;
const chute = input.questionInt('Digite seu palpite: ');

if (chute === numeroSecreto) {
    console.log('Parabéns! Você acertou!');
} else {
    console.log('Errado! O número secreto era', numeroSecreto);
}