function cl(s) {
  console.log(s)
};


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

function validateInput() {
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

document.getElementsByName('form')[0].onsubmit = function () {
  cl('submit');
  return validateInput();
};
