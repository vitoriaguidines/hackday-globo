import { SERVER_URL } from './constants.js';

export function filtrarComentarios(emoji) {
    fetch(`${SERVER_URL}/filtrar?emoji=${encodeURIComponent(emoji)}`)
        .then(response => response.json())
        .then(data => {
            const resultadosDiv = document.getElementById('resultados');
            resultadosDiv.innerHTML = ''; // Limpa os resultados anteriores

            if (data.comentarios.length > 0) {
                data.comentarios.forEach(comentario => {
                    const p = document.createElement('p');
                    p.textContent = comentario;
                    resultadosDiv.appendChild(p);
                });
            } else {
                resultadosDiv.textContent = 'Nenhum comentário encontrado.';
            }
        })
        .catch(error => console.error('Erro:', error));
}

// Adicionar event listeners para cada emoji
const emojis = [
    { id: 'emoji1', emoji: '🤬' },
    { id: 'emoji2', emoji: '☹️' },
    { id: 'emoji3', emoji: '😐' },
    { id: 'emoji4', emoji: '🙂' },
    { id: 'emoji5', emoji: '😀' }
];

emojis.forEach(item => {
    document.getElementById(item.id).addEventListener('click', () => filtrarComentarios(item.emoji));
});
