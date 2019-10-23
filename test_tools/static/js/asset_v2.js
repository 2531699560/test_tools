///////////////////IDC管理////////////////////
//获取编辑host信息

function test(){

    var case_id = document.getElementById('test');
    alert(case_id);
    //
    //     $.ajax({
    //     url: "/case/",
    //     type: "PUT",
    //     data: JSON.stringify({'case_id': case_id}),
    //     success: function (data) {
    //         if(data=="perms_false"){
    //             $("#msg-alert").empty();
    //             $("#msg-alert").append("权限不足，请联系管理员");
    //             $("#alert").show();
    //         }else {
    //
    //         var info = eval('(' + data + ')');
    //         $("#edit-host-ip").val(info.host_ip);
    //         $("#edit-host-remove-port").val(info.host_remove_port);
    //         $("#edit-host-user").val(info.host_user);
    //         $("#edit-host-passwd").val(info.host_passwd);
    //         $("#edit-host-type").val(info.host_type);
    //         $("#edit-host-group").val(info.host_group);
    //         $("#edit-host-idc").val(info.host_idc);
    //         $("#edit-host-supplier").val(info.host_supplier);
    //         $("#edit-host-msg").val(info.host_msg);
    //         $("#edit-host-serial-num").val(info.serial_num);
    //         $("#edit-host-purchase-date").val(info.purchase_date);
    //         $("#edit-host-overdue-date").val(info.overdue_date);
    //         $("#sub-edit-host").attr('host_id',info.host_id);
    //         $("#edit-hostModal").modal('show');
    //
    //         }
    //     }
    // });
}




$('td a[name="edit-host"]').click(function() {
    var case_id = $(this).attr("case_id");
    $.ajax({
        url: "/case/",
        type: "PUT",
        data: JSON.stringify({'case_id': case_id}),
        success: function (data) {
            if(data=="perms_false"){
                $("#msg-alert").empty();
                $("#msg-alert").append("权限不足，请联系管理员");
                $("#alert").show();
            }else {

            var info = eval('(' + data + ')');
            $("#edit-host-ip").val(info.host_ip);
            $("#edit-host-remove-port").val(info.host_remove_port);
            $("#edit-host-user").val(info.host_user);
            $("#edit-host-passwd").val(info.host_passwd);
            $("#edit-host-type").val(info.host_type);
            $("#edit-host-group").val(info.host_group);
            $("#edit-host-idc").val(info.host_idc);
            $("#edit-host-supplier").val(info.host_supplier);
            $("#edit-host-msg").val(info.host_msg);
            $("#edit-host-serial-num").val(info.serial_num);
            $("#edit-host-purchase-date").val(info.purchase_date);
            $("#edit-host-overdue-date").val(info.overdue_date);
            $("#sub-edit-host").attr('host_id',info.host_id);
            $("#edit-hostModal").modal('show');

            }
        }
    });
});
