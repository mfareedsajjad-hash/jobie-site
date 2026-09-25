/* ===== Jobie — Shared Script ===== */
function jobieToast(msg){
  let t=document.querySelector('.toast');
  if(!t){t=document.createElement('div');t.className='toast';document.body.appendChild(t);}
  t.textContent=msg;t.classList.add('show');
  clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('show'),2400);
}
// mobile nav
document.addEventListener('click',e=>{
  const h=e.target.closest('.hamburger');
  if(h)document.querySelector('.nav-links').classList.toggle('open');
});
// job filters (jobs page)
const jobsFilterForm=document.getElementById('jobsFilter');
if(jobsFilterForm){
  jobsFilterForm.addEventListener('submit',e=>{
    e.preventDefault();
    const q=document.getElementById('fSearch').value.toLowerCase();
    const cat=document.getElementById('fCategory').value;
    const loc=document.getElementById('fLocation').value;
    const type=document.getElementById('fType').value;
    let shown=0;
    document.querySelectorAll('.job-card').forEach(card=>{
      const text=card.textContent.toLowerCase();
      const okQ=!q||text.includes(q);
      const okC=!cat||card.dataset.category===cat;
      const okL=!loc||card.dataset.location===loc;
      const okT=!type||card.dataset.type===type;
      const ok=okQ&&okC&&okL&&okT;
      card.style.display=ok?'':'none';if(ok)shown++;
    });
    jobieToast(shown+' jobs found');
  });
  function resetFilters(){jobsFilterForm.reset();document.querySelectorAll('.job-card').forEach(c=>c.style.display='');jobieToast('Filters cleared');}
  const rb=document.getElementById('resetFilters');if(rb)rb.addEventListener('click',resetFilters);
}
// apply buttons
document.querySelectorAll('.apply-btn, .btn-apply').forEach(b=>{
  b.addEventListener('click',()=>{b.textContent='✓ Applied';b.classList.add('b-green','badge');jobieToast('Application submitted for '+ (b.dataset.job||'this job'));});
});
// save buttons
document.querySelectorAll('.save-btn').forEach(b=>{
  b.addEventListener('click',()=>{b.classList.toggle('saved');const on=b.classList.contains('saved');b.textContent=on?'♥ Saved':'♡ Save';jobieToast(on?'Job saved':'Removed from saved');});
});
// login form
const loginForm=document.getElementById('loginForm');
if(loginForm){loginForm.addEventListener('submit',e=>{e.preventDefault();location.href='dashboard.html';});}
// register form
const regForm=document.getElementById('registerForm');
if(regForm){regForm.addEventListener('submit',e=>{e.preventDefault();jobieToast('Account created! Please sign in.');setTimeout(()=>location.href='login.html',900);});}
// contact form
const contactForm=document.getElementById('contactForm');
if(contactForm){contactForm.addEventListener('submit',e=>{e.preventDefault();contactForm.reset();jobieToast('Message sent! We will reply soon.');});}
// dashboard nav
document.querySelectorAll('.dash-nav button').forEach(b=>{
  b.addEventListener('click',()=>{
    document.querySelectorAll('.dash-nav button').forEach(x=>x.classList.remove('active'));
    b.classList.add('active');
    const pn=document.getElementById('pageTitle');if(pn)pn.textContent=b.dataset.label;
    jobieToast(b.dataset.label+' section (demo view)');
  });
});
// sidebar login-link
const link=document.currentScript||{};
function headerFooter(){/* no-op */}
