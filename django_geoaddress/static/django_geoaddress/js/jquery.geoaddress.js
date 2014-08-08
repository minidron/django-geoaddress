$(document).ready(function() {

    /* Получить значение параметра объекта по его названию (рекурсивно) */
    function get_nested_item(name, obj) {
        if (typeof(obj) == 'object') {
            if (name in obj) {
                return obj[name];
            };
            for (var subobj in obj) {
                var result = get_nested_item(name, obj[subobj]);
                if (result) {
                    return result;
                }
            };
        };

        return '';
    };


    function get_name(obj) {
        return obj.GeoObject.metaDataProperty.GeocoderMetaData.text
    };


    function get_type(obj) {
        return obj.GeoObject.metaDataProperty.GeocoderMetaData.kind
    };


    function get_address_details(obj) {
        AddressDetails = {
            country: get_nested_item('CountryName', obj),
            area: get_nested_item('AdministrativeAreaName', obj),
            subarea: get_nested_item('SubAdministrativeAreaName', obj),
            locality: get_nested_item('LocalityName', obj),
            street: get_nested_item('ThoroughfareName', obj),
            house: get_nested_item('PremiseNumber', obj),
            coords: get_nested_item('pos', obj)
        }

        return AddressDetails;
    };


    function fill_address (obj, address) {
        var items = obj.closest('fieldset, .fieldset').find('[data-address-type]');

        $.each(items, function (index, el) {
            if ($(el).is('select')) {
                $('option', el).filter(function() {
                    return $(this).text() == address[$(el).attr('data-address-type')]; 
                }).prop('selected', true);
            } else {
                $(el).val( address[$(el).attr('data-address-type')] );
            };
        });
    }


    $('.geoaddress').each(function () {
        var geoaddress = $(this);

        geoaddress.autocomplete({
            serviceUrl: 'http://geocode-maps.yandex.ru/1.x/?format=json',
            dataType: 'jsonp',
            paramName: 'geocode',
            minChars: 1,
            deferRequestBy: 300,
            triggerSelectOnValidInput: false,
            transformResult: function (response) {
                response = response.response.GeoObjectCollection.featureMember;

                var suggestions = [];
                $.each(response, function (index, item) {
                    suggestions.push({
                        value: get_name(item),
                        data: item
                    });
                });

                return {
                    suggestions: suggestions
                }
            },
            onSelect: function (suggestion) {
                fill_address(geoaddress, get_address_details(suggestion.data));
            }
        });

    });


});
