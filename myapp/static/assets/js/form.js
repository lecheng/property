$('#datetimepicker1').datetimepicker({
    format:'MMM DD, YYYY',
});
$('#property-eng').change(function(){
    var id = this.selectedIndex;
    $('#property-chn').prop('selectedIndex',id);
});
$('#property-chn').change(function(){
    var id = this.selectedIndex;
    $('#property-eng').prop('selectedIndex',id);
})