$(document).ready(() => {
    // Add Item
    $('DIV#add_item').on('click', () => {
        $('UL.my_list').append('<li>Item</li>');
    });

    // Remove Last Item
    $('DIV#remove_item').on('click', () => {
        $('UL.my_list li:last').remove();
    });

    // Clear List
    $('DIV#clear_list').on('click', () => {
        $('UL.my_list').empty();
    });
});
