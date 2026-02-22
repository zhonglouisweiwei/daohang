/* ======================================================
   CHINR-OS V3.0 — 功能脚本
   ====================================================== */

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => document.querySelectorAll(sel);

const STORAGE_KEY = 'nav_bookmarks';
const CITY_KEY = 'nav_weather_city';
const ENGINE_KEY = 'nav_search_engine';
const SSH_KEY = 'nav_ssh_servers';
const MEMO_KEY = 'nav_calendar_memos';
const SETTINGS_KEY = 'nav_settings';

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
    { name: 'Google', url: 'https://www.google.com', group: '默认导航' },
    { name: 'Bilibili', url: 'https://www.bilibili.com', group: '默认导航' },
    { name: 'GitHub', url: 'https://github.com', group: '默认导航' },
    { name: '知乎', url: 'https://www.zhihu.com', group: '默认导航' },
    { name: 'YouTube', url: 'https://www.youtube.com', group: '默认导航' }
];

document.addEventListener('DOMContentLoaded', () => {
    initSettings();
    initClock();
    initWeather();
    initSearch();
    initBookmarks();
    initModals();
});

// ==================== 全局设置 ====================
function initSettings() {
    const defaultSettings = {
        cardScale: 1,
        themeColor1: '#ff2a5f',
        themeColor2: '#00d2ff'
    };

    let settings = defaultSettings;
    try {
        const stored = localStorage.getItem(SETTINGS_KEY);
        if (stored) settings = { ...defaultSettings, ...JSON.parse(stored) };
    } catch (e) { }

    // Apply settings on load
    applySettings(settings);

    // Initialize Modal Values
    $('#cardSizeSlider').value = settings.cardScale;
    $('#themeColor1').value = settings.themeColor1;
    $('#themeColor2').value = settings.themeColor2;

    // Live preview events
    $('#cardSizeSlider').addEventListener('input', (e) => {
        document.documentElement.style.setProperty('--card-scale', e.target.value);
    });
    $('#themeColor1').addEventListener('input', (e) => {
        document.documentElement.style.setProperty('--accent', e.target.value);
        document.documentElement.style.setProperty('--bg-mesh-1', e.target.value);
        // compute a transparent version for border
        document.documentElement.style.setProperty('--glass-border', e.target.value + '33'); // roughly 20% opacity hex
    });
    $('#themeColor2').addEventListener('input', (e) => {
        document.documentElement.style.setProperty('--bg-mesh-3', e.target.value);
    });

    // Save and Close
    $('#settingsConfirm').addEventListener('click', () => {
        const newSettings = {
            cardScale: parseFloat($('#cardSizeSlider').value),
            themeColor1: $('#themeColor1').value,
            themeColor2: $('#themeColor2').value
        };
        localStorage.setItem(SETTINGS_KEY, JSON.stringify(newSettings));
        $('#settingsModalOverlay').classList.remove('active');
    });
}

function applySettings(settings) {
    document.documentElement.style.setProperty('--card-scale', settings.cardScale);
    document.documentElement.style.setProperty('--accent', settings.themeColor1);
    document.documentElement.style.setProperty('--bg-mesh-1', settings.themeColor1);
    document.documentElement.style.setProperty('--glass-border', settings.themeColor1 + '33');
    document.documentElement.style.setProperty('--bg-mesh-3', settings.themeColor2);
}

// ==================== 时钟 & 日期 ====================
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
    $('#dateText').textContent = `${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日 ${days[now.getDay()]}`;

    const hour = now.getHours();
    let greeting = '你好';
    if (hour >= 5 && hour < 8) greeting = '🌅 早安，新的一天';
    else if (hour >= 8 && hour < 12) greeting = '☀️ 上午好，工作顺利';
    else if (hour >= 12 && hour < 14) greeting = '🌞 午休时间到';
    else if (hour >= 14 && hour < 18) greeting = '🌤️ 下午好';
    else if (hour >= 18 && hour < 22) greeting = '🌆 晚上好，该放松了';
    else greeting = '🌙 夜深了，注意休息';
    $('#greeting').textContent = greeting;
}

// ==================== 天气 ====================
function initWeather() {
    const city = localStorage.getItem(CITY_KEY) || 'Beijing';
    fetchWeather(city);

    $('#weatherIcon').addEventListener('click', () => {
        $('#cityInput').value = localStorage.getItem(CITY_KEY) || 'Beijing';
        $('#cityModalOverlay').classList.add('active');
    });
    $('#cityCancel').addEventListener('click', () => $('#cityModalOverlay').classList.remove('active'));
    $('#cityConfirm').addEventListener('click', () => {
        const city = $('#cityInput').value.trim();
        if (city) {
            localStorage.setItem(CITY_KEY, city);
            fetchWeather(city);
        }
        $('#cityModalOverlay').classList.remove('active');
    });
}

async function fetchWeather(city) {
    try {
        const resp = await fetch(`https://wttr.in/${encodeURIComponent(city)}?format=j1`);
        if (!resp.ok) throw new Error('API Error');
        const data = await resp.json();

        const current = data.current_condition[0];
        const desc = current.lang_zh && current.lang_zh[0] ? current.lang_zh[0].value : current.weatherDesc[0].value;
        const engDesc = current.weatherDesc[0].value;

        $('#weatherTemp').textContent = `${current.temp_C}°C`;
        $('#weatherDesc').textContent = desc;
        $('#weatherHumidity').textContent = `💧 ${current.humidity}%`;
        $('#weatherCity').textContent = `📍 ${city}`;
        $('#weatherIcon').textContent = WEATHER_ICONS[engDesc] || '🌡️';
    } catch {
        $('#weatherTemp').textContent = '--°C';
        $('#weatherDesc').textContent = '点击图标设置地名...';
        $('#weatherCity').textContent = `📍 ${city}`;
    }
}

// ==================== 搜索 ====================
function initSearch() {
    const saved = localStorage.getItem(ENGINE_KEY);
    if (saved) $('#searchEngine').value = saved;

    $('#searchEngine').addEventListener('change', () => localStorage.setItem(ENGINE_KEY, $('#searchEngine').value));

    const doSearch = () => {
        const q = $('#searchInput').value.trim();
        if (!q) return;
        window.open(SEARCH_ENGINES[$('#searchEngine').value] + encodeURIComponent(q), '_blank');
    };

    $('#searchBtn').addEventListener('click', doSearch);
    $('#searchInput').addEventListener('keydown', (e) => e.key === 'Enter' && doSearch());
}

// ==================== 书签导览 ====================
let bookmarks = [];
let manageMode = false;

function initBookmarks() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) { try { bookmarks = JSON.parse(stored); } catch { bookmarks = []; } }
    if (bookmarks.length === 0) {
        bookmarks = DEFAULT_BOOKMARKS.map(b => ({ ...b, id: uid() }));
        localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
    }
    renderCards();
    $('#manageBtn').addEventListener('click', () => {
        manageMode = !manageMode;
        $('#manageBtn').textContent = manageMode ? '完成' : '模式切换';
        $('#addCardBtn').style.display = manageMode ? 'block' : 'none';
        $('#cardGrid').parentElement.classList.toggle('manage-mode', manageMode);
    });

    // 导入书签功能
    $('#importBtn').addEventListener('click', () => {
        $('#importFile').click();
    });

    $('#importFile').addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (event) => {
            const htmlText = event.target.result;
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlText, 'text/html');
            const anchors = doc.querySelectorAll('a');

            let addedCount = 0;
            anchors.forEach(a => {
                const url = a.getAttribute('href');
                const name = a.textContent.trim();
                const icon = a.getAttribute('icon'); // Edge/Chrome exports base64 Favicons in 'icon' attribute

                let groupName = '导入书签'; // 默认导入分组
                const dl = a.closest('dl');
                if (dl) {
                    const prev = dl.previousElementSibling;
                    if (prev && prev.tagName === 'H3') {
                        groupName = prev.textContent.trim();
                    }
                }

                if (url && name) {
                    // Check if URL already exists to prevent duplicates
                    if (!bookmarks.some(b => b.url === url)) {
                        bookmarks.push({
                            id: uid(),
                            name,
                            url,
                            group: groupName,
                            customIcon: icon // Store the raw base64 icon if it exists
                        });
                        addedCount++;
                    }
                }
            });

            if (addedCount > 0) {
                localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
                renderCards();
                alert(`成功导入了 ${addedCount} 个书签！`);
            } else {
                alert('未找到新书签，可能已经全部导入过了。');
            }
            // clear the input so the same file can be selected again
            $('#importFile').value = '';
        };
        reader.readAsText(file);
    });
}

function renderCards() {
    const grid = $('#cardGrid');
    grid.innerHTML = '';

    // Grouping
    const groups = {};
    bookmarks.forEach(bm => {
        const g = bm.group || '默认导航';
        if (!groups[g]) groups[g] = [];
        groups[g].push(bm);
    });

    for (const [groupName, items] of Object.entries(groups)) {
        // Create title
        const title = document.createElement('div');
        title.className = 'bookmark-group-title';
        title.textContent = groupName;
        grid.appendChild(title);

        items.forEach(bm => {
            const div = document.createElement('a');
            div.className = 'bookmark-item';
            div.href = bm.url;
            div.target = '_blank';

            // Use custom icon if available (from import), otherwise fetch from Google
            const faviconSrc = bm.customIcon ? bm.customIcon : `https://www.google.com/s2/favicons?domain=${new URL(bm.url).hostname}&sz=64`;

            div.innerHTML = `
                <img class="bookmark-icon" src="${faviconSrc}" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' viewBox=\\'0 0 100 100\\'><rect fill=\\'%23666\\' width=\\'100\\' height=\\'100\\'/></svg>'">
                <span class="bookmark-name">${escapeHtml(bm.name)}</span>
                <button class="bm-edit" data-id="${bm.id}">✎</button>
                <button class="bm-del" data-id="${bm.id}">✕</button>
            `;

            div.querySelector('.bm-edit').addEventListener('click', (e) => {
                e.preventDefault(); e.stopPropagation();
                if (!manageMode) return;
                editingId = bm.id;
                $('#modalTitle').textContent = '编辑导航';
                $('#cardName').value = bm.name;
                $('#cardUrl').value = bm.url;
                $('#cardGroup').value = bm.group || '默认导航';
                $('#modalOverlay').classList.add('active');
            });

            div.querySelector('.bm-del').addEventListener('click', (e) => {
                e.preventDefault(); e.stopPropagation();
                if (!manageMode) return;
                if (confirm('确认删除?')) {
                    bookmarks = bookmarks.filter(b => b.id !== bm.id);
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
                    renderCards();
                }
            });

            grid.appendChild(div);
        });
    }
}

// ==================== 弹窗总管 ====================
let editingId = null;
let currentMemoDate = null;

function initModals() {
    // 关闭处理
    $$('.modal-overlay').forEach(el => el.addEventListener('click', (e) => { if (e.target === el) el.classList.remove('active'); }));
    $$('.btn-cancel').forEach(btn => btn.addEventListener('click', (e) => e.target.closest('.modal-overlay').classList.remove('active')));

    // 书签 Modal
    $('#addCardBtn').addEventListener('click', () => {
        editingId = null; $('#modalTitle').textContent = '添加导航';
        $('#cardName').value = ''; $('#cardUrl').value = ''; $('#cardGroup').value = '默认导航';
        $('#modalOverlay').classList.add('active');
    });

    // 设置 Modal
    $('#openSettingsBtn').addEventListener('click', () => {
        $('#settingsModalOverlay').classList.add('active');
    });

    $('#modalConfirm').addEventListener('click', () => {
        let name = $('#cardName').value.trim(), url = $('#cardUrl').value.trim(), group = $('#cardGroup').value.trim() || '默认导航';
        if (!name || !url) return;
        if (!/^https?:\/\//i.test(url)) url = 'https://' + url;

        if (editingId) {
            const bm = bookmarks.find(b => b.id === editingId);
            if (bm) { bm.name = name; bm.url = url; bm.group = group; }
        } else bookmarks.push({ id: uid(), name, url, group });

        localStorage.setItem(STORAGE_KEY, JSON.stringify(bookmarks));
        renderCards(); $('#modalOverlay').classList.remove('active');
    });
}

// utils
function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 7); }
function escapeHtml(str) { return str.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[c])); }
function escapeAttr(str) { return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;'); }
