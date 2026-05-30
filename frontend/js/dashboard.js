function renderOrders() {

    const dynamicOrders =
        JSON.parse(localStorage.getItem('galaxy_orders') || '[]');

    const staticOrders = [
        {
            id: '#ORD-8821',
            nama: 'Ajaraaa Aja',
            tanggal: '25 Mei 2026',
            total: 35000,
            status: 'process',
            label: 'Diproses'
        },
        {
            id: '#ORD-8790',
            nama: 'Mba Nai Nai',
            tanggal: '22 Mei 2026',
            total: 25000,
            status: 'success',
            label: 'Selesai'
        },
        {
            id: '#ORD-8755',
            nama: 'Aalfiraner',
            tanggal: '20 Mei 2026',
            total: 18000,
            status: 'success',
            label: 'Selesai'
        },
        {
            id: '#ORD-8740',
            nama: 'Siq Irwaner',
            tanggal: '18 Mei 2026',
            total: 30000,
            status: 'success',
            label: 'Selesai'
        }
    ];

    const allOrders = [...dynamicOrders, ...staticOrders];

    const tbody = document.querySelector('tbody');

    tbody.innerHTML = allOrders.map(order => `
        <tr>
            <td class="mono">${order.id}</td>
            <td class="bold">${order.nama}</td>
            <td>${order.tanggal}</td>
            <td class="bold">
                Rp ${order.total.toLocaleString('id-ID')}
            </td>
            <td>
                <span class="badge ${order.status}">
                    ${order.label}
                </span>
            </td>
        </tr>
    `).join('');
}

document.addEventListener('DOMContentLoaded', renderOrders);