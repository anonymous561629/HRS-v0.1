// Delete Property
const deleteBtn = document.querySelectorAll('.delete-btns');
deleteBtn.forEach((btn) => {
    btn.addEventListener('click', () => {
        const isDelete = confirm('Are you sure you want to delete this property?')
        if (isDelete) {
            const propertyId = btn.dataset.propertyid;
            window.location = '/accounts/manage_properties/delete/' + propertyId;
        }
    })
})
// Property Booking
const bookedBtn = document.querySelectorAll('.booked-btns');
bookedBtn.forEach((btn) => {
    btn.addEventListener('click', () => {
        const isBooked = confirm('Are you sure that this property is booked/Rented?')
        if (isBooked) {
            const propertyId = btn.dataset.propertyid
            window.location = '/accounts/manage_properties/book/' + propertyId;
        }   
    })
} )

