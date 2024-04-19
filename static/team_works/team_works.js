function select_page(member,url) {
    let username_val = $('#username').val()
    let checked_val = $('#checked').val()
    let select_human_val = member
    multi_post(url, {username: username_val, checked: checked_val, select_human: select_human_val});
  }

//POST転送メソッド
function multi_post(path, params, method='post') {

    const form = document.common_form;
    form.method = method;
    form.action = path;

    for (const key in params) {
    if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];

        form.appendChild(hiddenField);
    }
    }

    form.submit();
}