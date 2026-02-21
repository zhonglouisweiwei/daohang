/* ======================================================
   家用导航站 — 功能脚本 v2
   ====================================================== */

// ==================== 工具函数 ====================
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

// ==================== 常量 ====================
const STORAGE_KEY = 'nav_bookmarks';
const CITY_KEY = 'nav_weather_city';
const ENGINE_KEY = 'nav_search_engine';

const SEARCH_ENGINES = {
    google: 'https://www.google.com/search?q=',
    bing: 'https://www.bing.com/search?q=',
    duckduckgo: 'https://duckduckgo.com/?q='
};

const WEATHER_ICONS = {
    'Sunny': '☀️', 'Clear': '🌙',
    'Partly cloudy': '⛅', 'Partly Cloudy': '⛅',
    'Cloudy': '☁️', 'Overcast': '🌥️',
    'Mist': '🌫️', 'Fog': '🌫️',
    'Light rain': '🌦️', 'Light drizzle': '🌦️', 'Patchy light drizzle': '🌦️',
    'Moderate rain': '🌧️', 'Heavy rain': '🌧️',
    'Light snow': '🌨️', 'Moderate snow': '❄️', 'Heavy snow': '❄️',
    'Thundery outbreaks possible': '⛈️', 'Thunderstorm': '⛈️',
    'Patchy rain possible': '🌦️', 'Patchy light rain': '🌦️',
    'Light rain shower': '🌦️', 'Moderate or heavy rain shower': '🌧️',
};

const DEFAULT_BOOKMARKS = [
    { name: 'Google', url: 'https://www.google.com' },
    { name: 'Bilibili', url: 'https://www.bilibili.com' },
    { name: 'GitHub', url: 'https://github.com' },
    { name: '知乎', url: 'https://www.zhihu.com' },
    { name: '微博', url: 'https://weibo.com' },
    { name: '淘宝', url: 'https://www.taobao.com' },
    { name: 'YouTube', url: 'https://www.youtube.com' },
    { name: '网易云音乐', url: 'https://music.163.com' },
];

// ==================== 初始化 ====================
document.addEventListener('DOMContentLoaded', () => {
    initParticles();
    initClock();
    initCalendar();
    initWeather();
    initSearch();
    initBookmarks();
    initModals();
});

// ==================== 1. 背景粒子 ====================
function initParticles() {
    const container = $('#bgParticles');
    const count = 35;
    for (let i = 0; i < count; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        const size = Math.random() * 4 + 2;
        p.style.width = size + 'px';
        p.style.height = size + 'px';
        p.style.left = Math.random() * 100 + '%';
        p.style.animationDuration = (Math.random() * 20 + 15) + 's';
        p.style.animationDelay = (Math.random() * 20) + 's';
        container.appendChild(p);
    }
}

// ==================== 2. 时钟 & 日期 ====================
function initClock() {
    updateClock();
    setInterval(updateClock, 1000);
}

function updateClock() {
    const now = new Date();
    const h = String(now.getHours()).padStart(2, '0');
    const m = String(now.getMinutes()).padStart(2, '0');
    const s = String(now.getSeconds()).padStart(2, '0');
    $('#clock').textContent = `${h}:${m}:${s}`;

    const days = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
    const year = now.getFullYear();
    const month = now.getMonth() + 1;
    const date = now.getDate();
    const day = days[now.getDay()];
    $('#dateText').textContent = `${year}年${month}月${date}日 ${day}`;

    // 问候语
    const hour = now.getHours();
    let greeting = '你好';
    if (hour >= 5 && hour < 8) greeting = '🌅 早上好';
    else if (hour >= 8 && hour < 12) greeting = '☀️ 上午好';
    else if (hour >= 12 && hour < 14) greeting = '🌞 中午好';
    else if (hour >= 14 && hour < 18) greeting = '🌤️ 下午好';
    else if (hour >= 18 && hour < 22) greeting = '🌆 晚上好';
    else greeting = '🌙 夜深了，注意休息';
    $('#greeting').textContent = greeting;
}

// ==================== 3. 日历 ====================
let calYear, calMonth;

function initCalendar() {
    const now = new Date();
    calYear = now.getFullYear();
    calMonth = now.getMonth();
    renderCalendar();

    $('#calPrev').addEventListener('click', () => {
        calMonth--;
        if (calMonth < 0) { calMonth = 11; calYear--; }
        renderCalendar();
    });
    $('#calNext').addEventListener('click', () => {
        calMonth++;
        if (calMonth > 11) { calMonth = 0; calYear++; }
        renderCalendar();
    });
}

function renderCalendar() {
    const monthNames = ['1月', '2月', '3月', '4月', '5月', '6月',
        '7月', '8月', '9月', '10月', '11月', '12月'];
    $('#calTitle').textContent = `${calYear}年${monthNames[calMonth]}`;

    const firstDay = new Date(calYear, calMonth, 1).getDay();
    const daysInMonth = new Date(calYear, calMonth + 1, 0).getDate();
    const daysInPrev = new Date(calYear, calMonth, 0).getDate();

    const today = new Date();
    const isCurrentMonth = today.getFullYear() === calYear && today.getMonth() === calMonth;

    let html = '';
    let dayCount = 1;
    let nextDay = 1;

    const totalCells = Math.ceil((firstDay + daysInMonth) / 7) * 7;

    for (let i = 0; i < totalCells; i++) {
        if (i % 7 === 0) html += '<tr>';

        if (i < firstDay) {
            const d = daysInPrev - firstDay + i + 1;
            html += `<td class="other-month">${d}</td>`;
        } else if (dayCount <= daysInMonth) {
            const cls = (isCurrentMonth && dayCount === today.getDate()) ? ' class="today"' : '';
            html += `<td${cls}>${dayCount}</td>`;
            dayCount++;
        } else {
            html += `<td class="other-month">${nextDay}</td>`;
            nextDay++;
        }

        if (i % 7 === 6) html += '</tr>';
    }

    $('#calBody').innerHTML = html;
}

// ==================== 4. 天气 ====================
function initWeather() {
    const city = localStorage.getItem(CITY_KEY) || 'Beijing';
    fetchWeather(city);

    // 城市设置弹窗
    $('#weatherSettingsBtn').addEventListener('click', () => {
        $('#cityInput').value = localStorage.getItem(CITY_KEY) || 'Beijing';
        $('#cityModalOverlay').classList.add('active');
    });
    $('#cityCancel').addEventListener('click', () => {
        $('#cityModalOverlay').classList.remove('active');
    });
    $('#cityConfirm').addEventListener('click', () => {
        const city = $('#cityInput').value.trim();
        if (city) {
            localStorage.setItem(CITY_KEY, city);
            fetchWeather(city);
        }
        $('#cityModalOverlay').classList.remove('active');
    });
    $('#cityModalOverlay').addEventListener('click', (e) => {
        if (e.target === $('#cityModalOverlay')) {
            $('#cityModalOverlay').classList.remove('active');
        }
    });
}

async function fetchWeather(city) {
    try {
        const resp = await fetch(`https://wttr.in/${encodeURIComponent(city)}?format=j1`);
        if (!resp.ok) throw new Error('天气获取失败');
        const data = await resp.json();

        const current = data.current_condition[0];
        const tempC = current.temp_C;
        const desc = current.lang_zh && current.lang_zh[0] ? current.lang_zh[0].value : current.weatherDesc[0].value;
        const humidity = current.humidity;
        const windSpeed = current.windspeedKmph;
        const engDesc = current.weatherDesc[0].value;

        $('#weatherTemp').textContent = `${tempC}°C`;
        $('#weatherDesc').textContent = desc;
        $('#weatherHumidity').textContent = `💧 ${humidity}%`;
        $('#weatherWind').textContent = `🌬️ ${windSpeed} km/h`;
        $('#weatherCity').textContent = `📍 ${city}`;

        // 匹配图标
        const icon = WEATHER_ICONS[engDesc] || '🌡️';
        $('#weatherIcon').textContent = icon;
    } catch (err) {
        console.warn('天气加载失败:', err);
        $('#weatherDesc').textContent = '无法获取天气';
        $('#weatherTemp').textContent = '--°C';
    }
}

// ==================== 5. 搜索 ====================
function initSearch() {
    const saved = localStorage.getItem(ENGINE_KEY);
    if (saved && SEARCH_ENGINES[saved]) {
        $('#searchEngine').value = saved;
    }

    $('#searchEngine').addEventListener('change', () => {
        localStorage.setItem(ENGINE_KEY, $('#searchEngine').value);
    });

    const doSearch = () => {
        const q = $('#searchInput').value.trim();
        if (!q) return;
        const engine = $('#searchEngine').value;
        const url = SEARCH_ENGINES[engine] + encodeURIComponent(q);
        window.open(url, '_blank');
    };

    $('#searchBtn').addEventListener('click', doSearch);
    $('#searchInput').addEventListener('keydown', (e) => {
        if (e.key === 'Enter') doSearch();
    });
}

// ==================== 6. 导航卡片 ====================
let bookmarks = [];
let manageMode = false;

function initBookmarks() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
        try { bookmarks = JSON.parse(stored); } catch { bookmarks = []; }
    }
    if (bookmarks.length === 0) {
        bookmarks = DEFAULT_BOOKMARKS.map(b => ({ ...b, id: uid() }));
        saveBookmarks();
    }
    renderCards();

    // 管理按钮
    $('#manageBtn').addEventListener('click', toggleManageMode);
}

function saveBookmarks() {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
}

// ---- 拖拽状态 ----
let dragSrcIndex = null;

function renderCards() {
    const grid = $('#cardGrid');
    grid.innerHTML = '';
    bookmarks.forEach((bm, idx) => {
        const card = document.createElement('a');
        card.className = 'nav-card glass-card';
        card.href = bm.url;
        card.target = '_blank';
        card.rel = 'noopener noreferrer';
        card.style.animationDelay = `${idx * 0.05}s`;
        card.draggable = manageMode;
        card.dataset.index = idx;

        const favicon = getFaviconUrl(bm.url);
        const directFavicon = getDirectFaviconUrl(bm.url);
        const letterAvatar = generateLetterAvatar(bm.name);

        card.innerHTML = `
      <img class="card-icon" src="${favicon}" alt="${bm.name}"
           data-direct="${escapeAttr(directFavicon)}"
           data-letter="${escapeAttr(letterAvatar)}"
           onerror="if(this.dataset.direct && this.src!==this.dataset.direct){this.src=this.dataset.direct}else{this.src=this.dataset.letter}">
      <span class="card-title">${escapeHtml(bm.name)}</span>
      <button class="card-edit" title="编辑" data-id="${bm.id}">✎</button>
      <button class="card-delete" title="删除" data-id="${bm.id}">✕</button>
    `;

        // 编辑按钮
        card.querySelector('.card-edit').addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (!manageMode) return;
            openEditModal(bm.id);
        });

        // 删除按钮
        card.querySelector('.card-delete').addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (!manageMode) return;
            deleteCard(bm.id);
        });

        // ---- 拖拽事件（仅管理模式） ----
        card.addEventListener('dragstart', (e) => {
            if (!manageMode) { e.preventDefault(); return; }
            dragSrcIndex = idx;
            card.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
            e.dataTransfer.setData('text/plain', idx);
        });

        card.addEventListener('dragend', () => {
            card.classList.remove('dragging');
            $$('.nav-card.drag-over').forEach(c => c.classList.remove('drag-over'));
            dragSrcIndex = null;
        });

        card.addEventListener('dragover', (e) => {
            if (!manageMode) return;
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            if (parseInt(card.dataset.index) !== dragSrcIndex) {
                card.classList.add('drag-over');
            }
        });

        card.addEventListener('dragleave', () => {
            card.classList.remove('drag-over');
        });

        card.addEventListener('drop', (e) => {
            if (!manageMode) return;
            e.preventDefault();
            e.stopPropagation();
            card.classList.remove('drag-over');
            const fromIdx = dragSrcIndex;
            const toIdx = parseInt(card.dataset.index);
            if (fromIdx === null || fromIdx === toIdx) return;

            const [moved] = bookmarks.splice(fromIdx, 1);
            bookmarks.splice(toIdx, 0, moved);
            saveBookmarks();
            renderCards();
        });

        grid.appendChild(card);
    });
}

function toggleManageMode() {
    manageMode = !manageMode;
    const btn = $('#manageBtn');
    const addBtn = $('#addCardBtn');
    const grid = $('#cardGrid');

    btn.classList.toggle('active', manageMode);
    btn.querySelector('span').textContent = manageMode ? '完成' : '管理';
    addBtn.style.display = manageMode ? 'flex' : 'none';
    grid.parentElement.classList.toggle('manage-active', manageMode);

    // 更新卡片 draggable 属性
    $$('.nav-card').forEach(card => {
        card.draggable = manageMode;
    });
}

function openEditModal(id) {
    const bm = bookmarks.find(b => b.id === id);
    if (!bm) return;
    editingId = id;
    $('#modalTitle').textContent = '编辑导航卡片';
    $('#cardName').value = bm.name;
    $('#cardUrl').value = bm.url;
    const preview = $('#faviconPreview');
    const hint = $('#faviconHint');
    preview.src = getFaviconUrl(bm.url);
    preview.style.display = 'block';
    hint.style.display = 'none';
    $('#modalOverlay').classList.add('active');
    setTimeout(() => $('#cardName').focus(), 100);
}

function deleteCard(id) {
    if (!confirm('确定删除这个导航卡片吗？')) return;
    bookmarks = bookmarks.filter(b => b.id !== id);
    saveBookmarks();
    renderCards();
}

// 判断是否为内网地址
function isInternalUrl(url) {
    try {
        const hostname = new URL(url).hostname;
        // IP 地址段: 10.x, 172.16-31.x, 192.168.x, localhost, 或含端口的纯 IP
        if (/^(localhost|127\.|10\.|172\.(1[6-9]|2[0-9]|3[01])\.|192\.168\.)/.test(hostname)) return true;
        // 无 TLD 的内网主机名 (如 nas, router, synology)
        if (hostname.indexOf('.') === -1) return true;
        // .local / .lan / .home 等内网域名
        if (/\.(local|lan|home|internal|localdomain|intranet)$/i.test(hostname)) return true;
        return false;
    } catch {
        return false;
    }
}

// 主图标地址：内网走直接获取，外网走 Google API
function getFaviconUrl(url) {
    try {
        if (isInternalUrl(url)) {
            return getDirectFaviconUrl(url);
        }
        const domain = new URL(url).hostname;
        return `https://www.google.com/s2/favicons?domain=${domain}&sz=64`;
    } catch {
        return generateLetterAvatar('?');
    }
}

// 直接从站点根目录获取 favicon
function getDirectFaviconUrl(url) {
    try {
        const u = new URL(url);
        return `${u.protocol}//${u.host}/favicon.ico`;
    } catch {
        return '';
    }
}

// 根据名称首字生成彩色字母头像 (SVG data URI)
function generateLetterAvatar(name) {
    const letter = (name || '?').charAt(0).toUpperCase();
    // 根据字符生成稳定的色相
    let hash = 0;
    for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
    const hue = Math.abs(hash) % 360;
    const bg = `hsl(${hue}, 55%, 45%)`;
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
      <rect width="64" height="64" rx="12" fill="${bg}"/>
      <text x="32" y="32" dominant-baseline="central" text-anchor="middle"
            font-family="Inter,sans-serif" font-weight="600" font-size="28" fill="#fff">${letter}</text>
    </svg>`;
    return 'data:image/svg+xml,' + encodeURIComponent(svg);
}

// 转义 HTML 属性中的特殊字符
function escapeAttr(str) {
    return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;');
}

// ==================== 7. 弹窗管理 ====================
let editingId = null; // null = 添加模式, 有值 = 编辑模式

function initModals() {
    const overlay = $('#modalOverlay');
    const nameInput = $('#cardName');
    const urlInput = $('#cardUrl');
    const preview = $('#faviconPreview');
    const hint = $('#faviconHint');

    // 打开添加弹窗
    $('#addCardBtn').addEventListener('click', () => {
        editingId = null;
        $('#modalTitle').textContent = '添加导航卡片';
        nameInput.value = '';
        urlInput.value = '';
        preview.style.display = 'none';
        hint.style.display = '';
        overlay.classList.add('active');
        setTimeout(() => nameInput.focus(), 100);
    });

    // URL 输入实时预览图标
    let debounceTimer;
    urlInput.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
            const val = urlInput.value.trim();
            if (val && isValidUrl(val)) {
                preview.src = getFaviconUrl(val);
                preview.style.display = 'block';
                hint.style.display = 'none';
            } else {
                preview.style.display = 'none';
                hint.style.display = '';
            }
        }, 400);
    });

    // 取消
    $('#modalCancel').addEventListener('click', () => overlay.classList.remove('active'));
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) overlay.classList.remove('active');
    });

    // 确认（添加或编辑）
    $('#modalConfirm').addEventListener('click', () => {
        let name = nameInput.value.trim();
        let url = urlInput.value.trim();
        if (!name || !url) {
            shakeInput(!name ? nameInput : urlInput);
            return;
        }
        if (!/^https?:\/\//i.test(url)) url = 'https://' + url;
        if (!isValidUrl(url)) {
            shakeInput(urlInput);
            return;
        }

        if (editingId) {
            // 编辑模式
            const bm = bookmarks.find(b => b.id === editingId);
            if (bm) {
                bm.name = name;
                bm.url = url;
            }
        } else {
            // 添加模式
            bookmarks.push({ id: uid(), name, url });
        }
        saveBookmarks();
        renderCards();
        overlay.classList.remove('active');
        editingId = null;
    });
}

// ==================== 工具 ====================
function uid() {
    return Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
}

function escapeHtml(str) {
    const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
    return str.replace(/[&<>"']/g, c => map[c]);
}

function isValidUrl(str) {
    try { new URL(str); return true; } catch { return false; }
}

function shakeInput(el) {
    el.style.animation = 'none';
    el.offsetHeight; // force reflow
    el.style.animation = 'shake 0.4s ease';
    el.style.borderColor = '#ef4444';
    setTimeout(() => { el.style.borderColor = ''; el.style.animation = ''; }, 600);
}

// 添加 shake 动画到 head
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-6px); }
    40% { transform: translateX(6px); }
    60% { transform: translateX(-4px); }
    80% { transform: translateX(4px); }
  }
`;
document.head.appendChild(shakeStyle);
