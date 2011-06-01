function cl(s) {
  console.log(s)
};

// TODO: consider another format, like:
// RULES = [
//   {for : 'name', type: 'required', onerror: 'missingName'},
//   {...}
// ]

RULES = {
  name: {
     required: {
        onerror: 'missingName'
     },
     limit: {
        limit: 100,
        onerror: 'tooLongName'
     }
  },
  phone: {
     required: {
        onerror: 'missingPhone'
     },
     type: {
        type: 'phone',
        onerror: 'incorrectPhone'
     }
  },
  email: {
     required: {
        onerror: 'missingName'
     },
     type: {
        type: 'email',
        onerror: 'incorrectEmail'
     }
  }
}

function limit(val, args) {
  if (val.length > args.limit)
    return args.onerror
}

function required(val, args) {
  if (!val)
    return args.onerror
}

function type(val, args) {
  regexp = {
    phone: /^(\d{5,7}|(\(\d{3}\)|\d{3})\d{7}|\+\d{1,3}(\(\d{3}\)|\d{3})\d{7})$/,
    email: /^[-.\w]+@(?:[a-z\d][-a-z\d]+\.)+[a-z]{2,6}$/
  }[args.type];
  if (!val.match(regexp))
    return args.onerror
}

function bridge(rule, val, args) {
  f = {
    limit: limit,
    required: required,
    type: type
  }[rule]
  return f(val, args)
}

function validateAllInputs() {
  for (var field in RULES) {
    val = document.getElementsByName(field)[0].value
    for (var rule in RULES[field]) {
      var error = bridge(rule, val, RULES[field][rule])
      if (error) {
        console.log(error)
        alert(error)
        return false
      }
    }
  }
  return true
}

function validateInput(name) {
  var val = document.getElementsByName(name)[0].value,
      rule,
      error;

  for (rule in RULES[name]) {
    error = bridge(rule, val, RULES[name][rule]);
    if (error) {
      console.log(error);
      showError(error);
      return false;
    }
  }
  return true;
}

function showError(error) {
  alert(error);
};

document.getElementsByName('form')[0].onsubmit = function () {
  for (var name in RULES) {
    if (!validateInput(name)) { 
      return false;
    };
  };
};

var inputs = document.getElementsByTagName('input')
for (var i in inputs) {
  field = inputs[i]
  // field.onchange = 
  field.onblur = function (e) {
    e.stopPropagation();
    return validateInput(this.name);
  };
};
