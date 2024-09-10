function confirmerSuppression(event) {
    event.preventDefault(); // Empêche l'action par défaut du bouton

    // Afficher une boîte de confirmation
    const confirmation = confirm("Attention, vous êtes sur le point de supprimer cet élément ! Voulez-vous vraiment continuer ?");

    // Si l'utilisateur clique sur "OK", la suppression est confirmée
    if (confirmation) {
        alert('L\'élément a été supprimé.');
    } else {
        alert('Suppression annulée.');
    }
}

// Attacher l'événement de clic aux boutons "Supprimer"
document.querySelectorAll('button[style*="rgb(212, 21, 21)"]').forEach(button => {
    button.addEventListener('click', confirmerSuppression);
});
