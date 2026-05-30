function renderOrders() {
  const dynamic = JSON.parse(localStorage.getItem('galaxy_orders') || '[]');
  const staticRows = [ /* data #ORD-8821 dst. */ ];
  const all = [...dynamic, ...staticRows];
  const tbody = document.querySelector('table tbody');
  tbody.innerHTML = all.map(o => `
    <tr>
      <td class="mono">${o.id}</td>
      <td class="bold">${o.nama}</td>
      <td>${o.tanggal}</td>
      <td class="bold">Rp ${o.total.toLocaleString('id-ID')}</td>
      <td><span class="badge ${o.status}">${o.label}</span></td>
    </tr>`).join('');
}
document.addEventListener('DOMContentLoaded', renderOrders);