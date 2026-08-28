
console.log("Programa em JS");
alert("Programa em JS executado");

const nome =prompt("Informe seu nome: ")

const nota1 = Number(prompt("Informe a primeira nota: "));

const nota2 = Number(prompt("Informe a segunda nota: "));


const media = (nota1 + nota2) / 2;

const notamininma = 7;

let notarecuperacao = Number(0);

const resultado = media >= notarecuperacao || media >= notaminima ? "Aprovado" : "Reprovado";

if (media >= notamininma) {
    alert("Parabéns " + nome + ", você foi aprovado(a)!");
} else if (media >= 5 && media < notamininma) {
    notarecuperacao = Number(prompt("Informe a nota da recuperação: "));
    if (notarecuperacao >= notamininma) {
        alert("Parabéns " + nome + ", você foi aprovado(a) na recuperação!");
    } else {
        alert("Infelizmente " + nome + ", você foi reprovado(a).");
    }
}
 



console.log("Nome: "  + nome +" | "  + "Media: " + media  +" | " +"Nota 1: " + nota1 + " | " + "Nota 2: " + nota2 +" | " + "Nota de Recuperação: " + notarecuperacao +" | " + "Resultado: " + resultado);

