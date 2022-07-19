$(document).ready(function () {

    const sidebar = () => {
        if ($(window).width() < 1200) {
            $('#toggle-sidebar').on('click', event => {
                let self = event.currentTarget;
                $('#sidebar-panel').toggle(() => {
                });
                $(self).hide();
            });
            $('#sidebar-panel').on('click', '#close-sidebar', () => {
                $('#sidebar-panel').toggle(() => {
                });
                $('#toggle-sidebar').show();
            });
        }
    };
    sidebar();

    $('section').on('click', '.reservation', event => {
        let self = event.currentTarget;
        const service = $(self).closest('.service-row').attr('value');
        $('#reservation').val(service);
    });
});