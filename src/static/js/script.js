window.onload = function() {
    const ctx = document.getElementById('pie-chart').getContext('2d');
    const pieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Homme', 'Femme'],
            datasets: [{
                data: [50, 30], // Example data
                backgroundColor: ['#36A2EB', '#FF6384']
            }]
        },
        options: {
            responsive: true
        }
    });
};



// Fonction pour afficher la confirmation de suppression
function confirmerSuppression(event) {
    event.preventDefault(); // Empêche l'action par défaut du bouton

    // Afficher une boîte de confirmation
    const confirmation = confirm("Attention, vous êtes sur le point de supprimer cet élève ! Voulez-vous vraiment continuer ?");

    // Si l'utilisateur clique sur "OK", la suppression est confirmée
    if (confirmation) {
        // Ajoutez ici le code pour supprimer l'élève
        alert('L\'élève a été supprimé.');
    } else {
        // Si l'utilisateur clique sur "Annuler", la suppression est annulée
        alert('Suppression annulée.');
    }
}

// Attacher l'événement de clic aux boutons "Supprimer"
document.querySelectorAll('button[style*="rgb(212, 21, 21)"]').forEach(button => {
    button.addEventListener('click', confirmerSuppression);
});
