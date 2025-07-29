if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}
function ready() {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteImageModal"))
    
    document.getElementById('deleteimage').addEventListener('click', function () {
        deleteModal.show();
        })
}