$(document).ready(function() {
    const hardcodedDict = {
'Brazil': 0.75,
    'Brunei': 0.75,
    'China': 0.75,
    'Colombia': 0.75,
    'Cuba': 0.75,
    'Falkland Islands': 0.75,
    'Liechtenstein': 0.75,
    'Namibia': 0.75,
    'South Africa': 0.75,
    'South Korea': 0.75,
    'Suriname': 0.75,
    'Thailand': 0.75,
    'Turkey': 0.75,
    'Canada': 1.0,
    'Chile': 1.0,
    'Cyprus': 1.0,
    'Mexico': 1.0,
    'Moldova': 1.0,
    'North Macedonia': 1.0,
    'Portugal': 1.0,
    'USA': 1.0,
'Angola': 1.25,
    'Australia': 1.25,
    'Botswana': 1.25,
    'Costa Rica': 1.25,
    'Dominican Republic': 1.25,
    'Guam': 1.25,
    'Laos': 1.25,
    'Lebanon': 1.25,
    'Macau': 1.25,
    'Northern Mariana Islands': 1.25,
    'Peru': 1.25,
    'Poland': 1.25,
    'Qatar': 1.25,
    'Seychelles': 1.25,
    'Solomon Islands': 1.25,
 'Albania': 2.0,
    'Austria': 2.0,
    'Bahamas': 2.0,
    'Bahrain': 2.0,
    'Estonia': 2.0,
    'Faroe Islands': 2.0,
    'French Guiana': 2.0,
    'Honduras': 2.0,
    'Latvia': 2.0,
    'Netherlands Antilles': 2.0,
'Singapore': 2.8,
    'Spain': 2.8,
    'Switzerland': 2.8,
    'Uruguay': 2.8,
    'Maldives': 2.8,
    'UK': 2.8,
    'Andorra': 2.8,
    'Anguilla': 2.8,
    'Bosnia & Herzegovina': 2.8,
    'Denmark': 2.8,
    'Greece': 2.8,
    'Guinea-Bissau': 2.8,
    'Lithuania': 2.8,
    'Mozambique': 2.8,
    'Nicaragua': 2.8,
    'Paraguay': 2.8,
    'Puerto Rico': 2.8,
    'Romania': 2.8,
    'Slovakia': 2.8,
    'Sweden': 2.8,
 'Central African Republic': 3.25,
    'Czech Republic': 3.25,
    'Djibouti': 3.25,
    'Guadeloupe': 3.25,
    'Guernsey': 3.25,
    'Iceland': 3.25,
    'Italy': 3.25,
    'Japan': 3.25,
    'Montenegro': 3.25,
    'Norway': 3.25,
    'Reunion': 3.25,
    'Trinidad and Tobago': 3.25,
    'Venezuela': 3.25,
'Argentina': 3.75,
    'Dominica': 3.75,
    'El Salvador': 3.75,
    'France': 3.75,
    'Hong Kong': 3.75,
    'Hungary': 3.75,
    'Isle of Man': 3.75,
    'Malaysia': 3.75,
    'Montserrat': 3.75,
    'Swaziland': 3.75,
    'Zimbabwe': 3.75,
 'Aruba': 4.5,
    'Barbados': 4.5,
    'Belgium': 4.5,
    'Bolivia': 4.5,
    'Bulgaria': 4.5,
    'Burundi': 4.5,
    'Cape Verde': 4.5,
    'Cook Islands': 4.5,
    'Croatia': 4.5,
    'Equatorial Guinea': 4.5,
    'Finland': 4.5,
    'French Polynesia': 4.5,
    'Gibraltar': 4.5,
    'Guatemala': 4.5,
    'Guinea': 4.5,
    'Guyana': 4.5,
    'Ireland': 4.5,
    'Jersey': 4.5,
    'Liberia': 4.5,
    'Luxembourg': 4.5,
    'Malta': 4.5,
    'Netherlands': 4.5,
    'New Caledonia': 4.5,
    'New Zealand': 4.5,
    'Panama': 4.5,
    'Serbia': 4.5,
    'Sierra Leone': 4.5,
    'St Kitts & Nevis': 4.5,
 'Niger': 5.5,
    'Somalia': 5.5,
    'Taiwan': 5.5,
'UAE': 6.75,
    'Ivory Coast': 6.75,
    'Vietnam': 6.75,
 'Antigua and Barbuda': 7.25,
    'Armenia': 7.25,
    'Burkina Faso': 7.25,
    'Cameroon': 7.25,
    'Chad': 7.25,
    'Ecuador': 7.25,
    'Eritrea': 7.25,
    'Fiji': 7.25,
    'Gambia': 7.25,
    'Georgia': 7.25,
    'Germany': 7.25,
    'Grenada': 7.25,
    'Haiti': 7.25,
    'Iran': 7.25,
    'Kenya': 7.25,
    'Kuwait': 7.25,
    'Lesotho': 7.25,
    'Madagascar': 7.25,
    'Mali': 7.25,
    'Mongolia': 7.25,
    'Morocco': 7.25,
    'Oman': 7.25,
    'Saudi Arabia': 7.25,
    'Slovenia': 7.25,
    'South Sudan': 7.25,
    'St. Vincent and Grenadines': 7.25,
    'Vanuatu': 7.25,
    'Virgin Islands British': 7.25,
 'Turks and Caicos': 10,
    'Papua New Guinea': 10,
    'Algeria': 10,
    'Benin': 10,
    'Bermuda': 10,
    'Cambodia': 10,
    'Cayman Islands': 10,
    'Comoros': 10,
    'Democratic Republic of Congo': 10,
    'Egypt': 10,
    'Gabon': 10,
    'Ghana': 10,
    'Mauritania': 10,
    'Mauritius': 10,
    'Nepal': 10,
    'Philippines': 10,
    'Togo': 10,
    'Tunisia': 10,
    'Turkmenistan': 10,
    'Ukraine': 10,
 'Belize': 13,
    'Bhutan': 13,
    'Republic of Congo': 13,
    'Ethiopia': 13,
    'Israel': 13,
    'Jamaica': 13,
    'Jordan': 13,
    'Kazakhstan': 13,
    'Libya': 13,
    'Malawi': 13,
    'Myanmar': 13,
    'Nigeria': 13,
    'Rwanda': 13,
    'Senegal': 13,
    'Syria': 13,
    'Tanzania': 13,
    'Yemen Arab Republic': 13,
    'Zambia': 13,
 'Afghanistan': 16,
    'Bangladesh': 16,
    'Belarus': 16,
    'Iraq': 16,
    'Kyrgyzstan': 16,
    'Palestinian Territory': 16,
    'Sri Lanka': 16,
    'Sudan': 16,
    'Uganda': 16,
 'Indonesia': 25,
    'Pakistan': 25,
    'Russia': 25,
    'Tajikistan': 25,
    'Uzbekistan': 25,
    'Azerbaijan': 25
    };

    function compareDicts(inputDict, hardcodedDict) {
        let keys = new Set(Object.keys(inputDict).concat(Object.keys(hardcodedDict)));
        let comparison = [];
        let changes = [];

        keys.forEach(key => {
            let inputValue = inputDict[key] !== undefined ? inputDict[key] : 'NA';
            let hardcodedValue = hardcodedDict[key] !== undefined ? hardcodedDict[key] : 'NA';
            let match = inputValue == hardcodedValue;

            comparison.push({key, inputValue, hardcodedValue, match});

            if (!match) {
                changes.push({key, inputValue, hardcodedValue});
            }
        });

        return {comparison, changes};
    }

    function renderTable(data, selector) {
        let table = `<table>
            <thead>
                <tr>
                    <th>Key</th>
                    <th>Input Value</th>
                    <th>Hardcoded Value</th>
                </tr>
            </thead>
            <tbody>`;

        data.forEach(row => {
            let highlightClass = '';
            if (row.inputValue === 'NA' || row.hardcodedValue === 'NA') {
                highlightClass = 'highlight-red';
            } else if (!row.match) {
                highlightClass = 'highlight-yellow';
            }

            table += `<tr class="${highlightClass}">
                <td>${row.key}</td>
                <td>${row.inputValue}</td>
                <td>${row.hardcodedValue}</td>
            </tr>`;
        });

        table += `</tbody></table>`;
        $(selector).html(table);
    }

    function renderChangesTable(data, viewOption) {
        let filteredData = data;

        if (viewOption === 'Non-Available data only') {
            filteredData = data.filter(row => row.inputValue === 'NA' || row.hardcodedValue === 'NA');
        } else if (viewOption === 'Input changes only') {
            filteredData = data.filter(row => row.inputValue !== 'NA' && row.hardcodedValue !== 'NA');
        }

        renderTable(filteredData, '#changes-table');
    }

    function renderBarChart(data) {
        let keys = data.map(row => row.key);
        let inputValues = data.map(row => parseFloat(row.inputValue));
        let hardcodedValues = data.map(row => parseFloat(row.hardcodedValue));

        new Chart($('#bar-chart'), {
            type: 'bar',
            data: {
                labels: keys,
                datasets: [
                    {
                        label: 'Input Value',
                        data: inputValues,
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    },
                    {
                        label: 'Hardcoded Value',
                        data: hardcodedValues,
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    }
                ]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    $('#compare-button').click(function() {
        let inputText = $('#input-text').val();
        try {
            let inputDict = JSON.parse(inputText.replace(/'/g, '"'));

            if (typeof inputDict === 'object') {
                let {comparison, changes} = compareDicts(inputDict, hardcodedDict);

                renderTable(comparison, '#comparison-table');
                renderChangesTable(changes, $('input[name="view-option"]:checked').val());

                let numericChanges = changes.filter(row => !isNaN(parseFloat(row.inputValue)) && !isNaN(parseFloat(row.hardcodedValue)));
                if (numericChanges.length > 0) {
                    renderBarChart(numericChanges);
                } else {
                    $('#bar-chart').hide();
                }
            } else {
                alert('Please enter a valid dictionary.');
            }
        } catch (e) {
            alert('Error parsing input dictionary: ' + e.message);
        }
    });

    $('input[name="view-option"]').change(function() {
        let changes = compareDicts(JSON.parse($('#input-text').val().replace(/'/g, '"')), hardcodedDict).changes;
        renderChangesTable(changes, $(this).val());
    });
});
