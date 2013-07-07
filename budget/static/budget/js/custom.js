function append_sequence_selects() {
    $('#sequence').empty();
    var length = parseInt($('#program_length').val());
    var current = parseInt($('#current_year').val());
    var coop = $('#coop').val() == 'True' ? 1 : 0;

    for (var i = 0; i <= length - current; i++) {
        var div_str = '';
        var year = i + current;
        if (coop) {
            div_str =   '<div class="control-group">' +
                            '<label class="control-label" for="'+year+'_sequence">Year '+year+' Sequence</label>' +
                            '<div class="controls">' +
                                '<select id="'+year+'_sequence" name="'+year+'_sequence" >' + 
                                    '<option value="SSW">Study, Study, Work</option>' +
                                    '<option value="SWW">Study, Work, Work</option>' +
                                    '<option value="SWS">Study, Work, Study</option>' +
                                    '<option value="SSS">Study, Study, Study</option>' +
                                    '<option value="WSS">Work, Study, Study</option>' +
                                    '<option value="WSW">Work, Study, Work</option>' +
                                    '<option value="WWS">Work, Work, Study</option>' +
                                '</select>' +
                            '</div>' +
                        '</div>';
        } else {
            div_str =   '<div class="control-group">' +
                            '<label class="control-label" for="'+year+'_sequence">Year '+year+' Sequence</label>' +
                            '<div class="controls">' +
                                '<select id="'+year+'_sequence" name="'+year+'_sequence" >' +
                                    '<option value="SSS">Study, Study, Study</option>' +
                                    '<option value="SSO">Study, Study, Off</option>' +
                                    '<option value="SOS">Study, Off, Study</option>' +
                                    '<option value="OSS">Off, Study, Study</option>' +
                                '</select>' +
                            '</div>' +
                        '</div>';
        }
        $('#sequence').append(div_str);
    }
}