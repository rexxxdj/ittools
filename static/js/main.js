function initJournal() {
    $('.day-box input[type="checkbox"]').click(function (event) {
        var box = $(this);        
        $.ajax(box.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('unit-id'),
                'date': box.data('date'),
                'jid': box.data('jid'),
                'day': box.data('day'),
                'present': box.is(':checked') ? '1': '',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },            
            'error': function(xhr, status, error){                    
                alert(error);
            },
            'success': function(data, status, xhr){
                if (data['text'] != ''){
                    alert(data['text']);
                }
            }
        });
    });
}

$(document).ready(function () {
    initJournal();
});