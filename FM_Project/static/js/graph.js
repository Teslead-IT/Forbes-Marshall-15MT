window.onload = function() {
    fetch('/sales_data/')  // Assuming you have the URL for your sales data
        .then(response => response.json())
        .then(data => {
            const labels = data.labels;
            const salesData = data.data.map(item => parseInt(item, 10));

            const ctx = document.getElementById('myChart').getContext('2d');

            new Chart(ctx, {
                type: 'bar',  // Or 'line', 'pie', etc.
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Monthly Sales',
                        data: salesData,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
}
