function populateDropdowns() {
    var baseUrl = "http://127.0.0.1:5000";
    $.get(baseUrl + "/get_brand_names", function (data) {
      var brands = data.brands;
      brands.forEach(function (brand) {
        $("#brand").append(new Option(brand, brand));
      });
    });
  
    $.get(baseUrl + "/get_interior_names", function (data) {
      var interiors = data.interiors;
      interiors.forEach(function (interior) {
        $("#interior").append(new Option(interior, interior));
      });
    });
  
    $.get(baseUrl + "/get_exterior_names", function (data) {
      var exteriors = data.exteriors;
      exteriors.forEach(function (exterior) {
        $("#exterior").append(new Option(exterior, exterior));
      });
    });
  }
  
  function onClickedEstimatePrice() {
    var baseUrl = "http://127.0.0.1:5000";
    var brand = $("#brand").val();
    var interior = $("#interior").val();
    var exterior = $("#exterior").val();
    var age = $("#age").val();
    var miles = $("#miles").val();
    var accidents = $("#accidents").val();
    var owners = $("#owners").val();
  
    $.post(
      baseUrl + "/predict_car_price",
      {
        brand: brand,
        interior: interior,
        exterior: exterior,
        age: age,
        miles: miles,
        accidents: accidents,
        owners: owners,
      },
      function (data) {
        $("#estimatedPrice span").text(data.estimated_price);
      }
    );
  }
  
  $(document).ready(function () {
    populateDropdowns();
  });
  