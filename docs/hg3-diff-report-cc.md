# HG3 红果 v7.3.7.32 外层 dex 全量 diff 报告（外层 24 dex vs 内嵌官方原包 22 dex）

> 方法=类名对齐+调试指令剥离（继承番茄 round16a 两轮修正）。分类权在老马：
> A=壳代码(番茄画像重合) / B=去广告会员patch / C=可疑新增(番茄壳中不存在) / D=VIP伪造保留

## 1. 总览

- 外层类总数: 290644 ｜ 内层官方类总数: 289416
- **真新增类: 1228**（全文见 hg3-diff-baksmali/added/）
- **真删除类: 0**（全文见 hg3-diff-baksmali/removed/）
- **修改类: 3527**（差异方法全文见 hg3-diff-baksmali/changed/，[MOD-ADDED]/[MOD-CHANGED vs INNER-ORIGINAL]/[INNER-REMOVED-IN-MOD] 三段标注）
- 修改类中差异方法: 新增 14506 / 删除 30 / 修改 10408

- 跨 dex 重复类名（mod）: 0 ｜（inner）: 0（应为 0，非 0 需在报告红旗解释）

## 2. 真新增类清单（按包前缀分组）

### `com/` — 1082 类
- `com/A.smali`
- `com/B.smali`
- `com/C.smali`
- `com/D.smali`
- `com/E.smali`
- `com/F.smali`
- `com/G.smali`
- `com/H.smali`
- `com/I.smali`
- `com/J.smali`
- `com/K.smali`
- `com/L.smali`
- `com/M.smali`
- `com/N.smali`
- `com/O.smali`
- `com/P.smali`
- `com/Q.smali`
- `com/R.smali`
- `com/S.smali`
- `com/T.smali`
- `com/U.smali`
- `com/V.smali`
- `com/W.smali`
- `com/X.smali`
- `com/Y.smali`
- `com/Z.smali`
- `com/aA.smali`
- `com/aB.smali`
- `com/aC.smali`
- `com/aD.smali`
- `com/aE.smali`
- `com/aF.smali`
- `com/aG.smali`
- `com/aH.smali`
- `com/aI.smali`
- `com/aJ.smali`
- `com/aK.smali`
- `com/aL.smali`
- `com/aM.smali`
- `com/aN.smali`
- `com/aO.smali`
- `com/aP.smali`
- `com/aQ.smali`
- `com/aR.smali`
- `com/aS.smali`
- `com/aT.smali`
- `com/aU.smali`
- `com/aV.smali`
- `com/aW.smali`
- `com/aX.smali`
- `com/aY.smali`
- `com/aZ.smali`
- `com/aa.smali`
- `com/ab.smali`
- `com/ac.smali`
- `com/ad.smali`
- `com/ae.smali`
- `com/af.smali`
- `com/ag.smali`
- `com/ah.smali`
- `com/ai.smali`
- `com/aj.smali`
- `com/ak.smali`
- `com/al.smali`
- `com/am.smali`
- `com/an.smali`
- `com/ao.smali`
- `com/ap.smali`
- `com/aq.smali`
- `com/ar.smali`
- `com/as.smali`
- `com/at.smali`
- `com/au.smali`
- `com/av.smali`
- `com/aw.smali`
- `com/ax.smali`
- `com/ay.smali`
- `com/az.smali`
- `com/bA.smali`
- `com/bB.smali`
- `com/bC.smali`
- `com/bD.smali`
- `com/bE.smali`
- `com/bF.smali`
- `com/bG.smali`
- `com/bH.smali`
- `com/bI.smali`
- `com/bJ.smali`
- `com/bK.smali`
- `com/bL.smali`
- `com/bM.smali`
- `com/bN.smali`
- `com/bO.smali`
- `com/bP.smali`
- `com/bQ.smali`
- `com/bR.smali`
- `com/bS.smali`
- `com/bT.smali`
- `com/bU.smali`
- `com/bV.smali`
- `com/bW.smali`
- `com/bX.smali`
- `com/bY.smali`
- `com/bZ.smali`
- `com/ba.smali`
- `com/bb.smali`
- `com/bc.smali`
- `com/bd.smali`
- `com/be.smali`
- `com/bf.smali`
- `com/bg.smali`
- `com/bh.smali`
- `com/bi.smali`
- `com/bj.smali`
- `com/bk.smali`
- `com/bl.smali`
- `com/bm.smali`
- `com/bn.smali`
- `com/bo.smali`
- `com/bp.smali`
- `com/bq.smali`
- `com/br.smali`
- `com/bs.smali`
- `com/bt.smali`
- `com/bu.smali`
- `com/bv.smali`
- `com/bw.smali`
- `com/bx.smali`
- `com/by.smali`
- `com/bz.smali`
- `com/cA.smali`
- `com/cB.smali`
- `com/cC.smali`
- `com/cD.smali`
- `com/cE.smali`
- `com/cF.smali`
- `com/cG.smali`
- `com/cH.smali`
- `com/cI.smali`
- `com/cJ.smali`
- `com/cK.smali`
- `com/cL.smali`
- `com/cM.smali`
- `com/cN.smali`
- `com/cO.smali`
- `com/cP.smali`
- `com/cQ.smali`
- `com/cR.smali`
- `com/cS.smali`
- `com/cT.smali`
- `com/cU.smali`
- `com/cV.smali`
- `com/cW.smali`
- `com/cX.smali`
- `com/cY.smali`
- `com/cZ.smali`
- `com/ca.smali`
- `com/cb.smali`
- `com/cc.smali`
- `com/cd.smali`
- `com/ce.smali`
- `com/cf.smali`
- `com/cg.smali`
- `com/ch.smali`
- `com/ci.smali`
- `com/cj.smali`
- `com/ck.smali`
- `com/cl.smali`
- `com/cm.smali`
- `com/cn.smali`
- `com/co.smali`
- `com/cp.smali`
- `com/cq.smali`
- `com/cr.smali`
- `com/cs.smali`
- `com/ct.smali`
- `com/cu.smali`
- `com/cv.smali`
- `com/cw.smali`
- `com/cx.smali`
- `com/cy.smali`
- `com/cz.smali`
- `com/dA.smali`
- `com/dB.smali`
- `com/dC.smali`
- `com/dD.smali`
- `com/dE.smali`
- `com/dF.smali`
- `com/dG.smali`
- `com/dH.smali`
- `com/dI.smali`
- `com/dJ.smali`
- `com/dK.smali`
- `com/dL.smali`
- `com/dM.smali`
- `com/dN.smali`
- `com/dO.smali`
- `com/dP.smali`
- `com/dQ.smali`
- `com/dR.smali`
- `com/dS.smali`
- `com/dT.smali`
- `com/dU.smali`
- `com/dV.smali`
- `com/dW.smali`
- `com/dX.smali`
- `com/dY.smali`
- `com/dZ.smali`
- `com/da.smali`
- `com/db.smali`
- `com/dc.smali`
- `com/dd.smali`
- `com/de.smali`
- `com/df.smali`
- `com/dg.smali`
- `com/dh.smali`
- `com/di.smali`
- `com/dj.smali`
- `com/dk.smali`
- `com/dl.smali`
- `com/dm.smali`
- `com/dn.smali`
- `com/do.smali`
- `com/dp.smali`
- `com/dq.smali`
- `com/dr.smali`
- `com/ds.smali`
- `com/dt.smali`
- `com/du.smali`
- `com/dv.smali`
- `com/dw.smali`
- `com/dx.smali`
- `com/dy.smali`
- `com/dz.smali`
- `com/eA.smali`
- `com/eB.smali`
- `com/eC.smali`
- `com/eD.smali`
- `com/eE.smali`
- `com/eF.smali`
- `com/eG.smali`
- `com/eH.smali`
- `com/eI.smali`
- `com/eJ.smali`
- `com/eK.smali`
- `com/eL.smali`
- `com/eM.smali`
- `com/eN.smali`
- `com/eO.smali`
- `com/eP.smali`
- `com/eQ.smali`
- `com/eR.smali`
- `com/eS.smali`
- `com/eT.smali`
- `com/eU.smali`
- `com/eV.smali`
- `com/eW.smali`
- `com/eX.smali`
- `com/eY.smali`
- `com/eZ.smali`
- `com/ea.smali`
- `com/eb.smali`
- `com/ec.smali`
- `com/ed.smali`
- `com/ee.smali`
- `com/ef.smali`
- `com/eg.smali`
- `com/eh.smali`
- `com/ei.smali`
- `com/ej.smali`
- `com/ek.smali`
- `com/el.smali`
- `com/em.smali`
- `com/en.smali`
- `com/eo.smali`
- `com/ep.smali`
- `com/eq.smali`
- `com/er.smali`
- `com/es.smali`
- `com/et.smali`
- `com/eu.smali`
- `com/ev.smali`
- `com/ew.smali`
- `com/ex.smali`
- `com/ey.smali`
- `com/ez.smali`
- `com/fA.smali`
- `com/fB.smali`
- `com/fC.smali`
- `com/fD.smali`
- `com/fE.smali`
- `com/fF.smali`
- `com/fG.smali`
- `com/fH.smali`
- `com/fI.smali`
- `com/fJ.smali`
- `com/fK.smali`
- `com/fL.smali`
- `com/fM.smali`
- `com/fN.smali`
- `com/fO.smali`
- `com/fP.smali`
- `com/fQ.smali`
- `com/fR.smali`
- `com/fS.smali`
- `com/fT.smali`
- `com/fU.smali`
- `com/fV.smali`
- `com/fW.smali`
- `com/fX.smali`
- `com/fY.smali`
- `com/fZ.smali`
- `com/fa.smali`
- `com/fb.smali`
- `com/fc.smali`
- `com/fd.smali`
- `com/fe.smali`
- `com/ff.smali`
- `com/fg.smali`
- `com/fh.smali`
- `com/fi.smali`
- `com/fj.smali`
- `com/fk.smali`
- `com/fl.smali`
- `com/fm.smali`
- `com/fn.smali`
- `com/fo.smali`
- `com/fp.smali`
- `com/fq.smali`
- `com/fr.smali`
- `com/fs.smali`
- `com/ft.smali`
- `com/fu.smali`
- `com/fv.smali`
- `com/fw.smali`
- `com/fx.smali`
- `com/fy.smali`
- `com/fz.smali`
- `com/gA.smali`
- `com/gB.smali`
- `com/gC.smali`
- `com/gD.smali`
- `com/gE.smali`
- `com/gF.smali`
- `com/gG.smali`
- `com/gH.smali`
- `com/gI.smali`
- `com/gJ.smali`
- `com/gK.smali`
- `com/gL.smali`
- `com/gM.smali`
- `com/gN.smali`
- `com/gO.smali`
- `com/gP.smali`
- `com/gQ.smali`
- `com/gR.smali`
- `com/gS.smali`
- `com/gT.smali`
- `com/gU.smali`
- `com/gV.smali`
- `com/gW.smali`
- `com/gX.smali`
- `com/gY.smali`
- `com/gZ.smali`
- `com/ga.smali`
- `com/gb.smali`
- `com/gc.smali`
- `com/gd.smali`
- `com/ge.smali`
- `com/gf.smali`
- `com/gg.smali`
- `com/gh.smali`
- `com/gi.smali`
- `com/gj.smali`
- `com/gk.smali`
- `com/gl.smali`
- `com/gm.smali`
- `com/gn.smali`
- `com/go.smali`
- `com/gp.smali`
- `com/gq.smali`
- `com/gr.smali`
- `com/gs.smali`
- `com/gt.smali`
- `com/gu.smali`
- `com/gv.smali`
- `com/gw.smali`
- `com/gx.smali`
- `com/gy.smali`
- `com/gz.smali`
- `com/hA.smali`
- `com/hB.smali`
- `com/hC.smali`
- `com/hD.smali`
- `com/hE.smali`
- `com/hF.smali`
- `com/hG.smali`
- `com/hH.smali`
- `com/hI.smali`
- `com/hJ.smali`
- `com/hK.smali`
- `com/hL.smali`
- `com/hM.smali`
- `com/hN.smali`
- `com/hO.smali`
- `com/hP.smali`
- `com/hQ.smali`
- `com/hR.smali`
- `com/hS.smali`
- `com/hT.smali`
- `com/hU.smali`
- `com/hV.smali`
- `com/hW.smali`
- `com/hX.smali`
- `com/hY.smali`
- `com/hZ.smali`
- `com/ha.smali`
- `com/hb.smali`
- `com/hc.smali`
- `com/hd.smali`
- `com/he.smali`
- `com/hf.smali`
- `com/hg.smali`
- `com/hh.smali`
- `com/hi.smali`
- `com/hj.smali`
- `com/hk.smali`
- `com/hl.smali`
- `com/hm.smali`
- `com/hn.smali`
- `com/ho.smali`
- `com/hp.smali`
- `com/hq.smali`
- `com/hr.smali`
- `com/hs.smali`
- `com/ht.smali`
- `com/hu.smali`
- `com/hv.smali`
- `com/hw.smali`
- `com/hx.smali`
- `com/hy.smali`
- `com/hz.smali`
- `com/iA.smali`
- `com/iB.smali`
- `com/iC.smali`
- `com/iD.smali`
- `com/iE.smali`
- `com/iF.smali`
- `com/iG.smali`
- `com/iH.smali`
- `com/iI.smali`
- `com/iJ.smali`
- `com/iK.smali`
- `com/iL.smali`
- `com/iM.smali`
- `com/iN.smali`
- `com/iO.smali`
- `com/iP.smali`
- `com/iQ.smali`
- `com/iR.smali`
- `com/iS.smali`
- `com/iT.smali`
- `com/iU.smali`
- `com/iV.smali`
- `com/iW.smali`
- `com/iX.smali`
- `com/iY.smali`
- `com/iZ.smali`
- `com/ia.smali`
- `com/ib.smali`
- `com/ic.smali`
- `com/id.smali`
- `com/ie.smali`
- `com/if.smali`
- `com/ig.smali`
- `com/ih.smali`
- `com/ii.smali`
- `com/ij.smali`
- `com/ik.smali`
- `com/il.smali`
- `com/im.smali`
- `com/in.smali`
- `com/io.smali`
- `com/ip.smali`
- `com/iq.smali`
- `com/ir.smali`
- `com/is.smali`
- `com/it.smali`
- `com/iu.smali`
- `com/iv.smali`
- `com/iw.smali`
- `com/ix.smali`
- `com/iy.smali`
- `com/iz.smali`
- `com/j.smali`
- `com/jA.smali`
- `com/jB.smali`
- `com/jC.smali`
- `com/jD.smali`
- `com/jE.smali`
- `com/jF.smali`
- `com/jG.smali`
- `com/jH.smali`
- `com/jI.smali`
- `com/jJ.smali`
- `com/jK.smali`
- `com/jL.smali`
- `com/jM.smali`
- `com/jN.smali`
- `com/jO.smali`
- `com/jP.smali`
- `com/jQ.smali`
- `com/jR.smali`
- `com/jS.smali`
- `com/jT.smali`
- `com/jU.smali`
- `com/jV.smali`
- `com/jW.smali`
- `com/jX.smali`
- `com/jY.smali`
- `com/jZ.smali`
- `com/ja.smali`
- `com/jb.smali`
- `com/jc.smali`
- `com/jd.smali`
- `com/je.smali`
- `com/jf.smali`
- `com/jg.smali`
- `com/jh.smali`
- `com/ji.smali`
- `com/jj.smali`
- `com/jk.smali`
- `com/jl.smali`
- `com/jm.smali`
- `com/jn.smali`
- `com/jo.smali`
- `com/jp.smali`
- `com/jq.smali`
- `com/jr.smali`
- `com/js.smali`
- `com/jt.smali`
- `com/ju.smali`
- `com/jv.smali`
- `com/jw.smali`
- `com/jx.smali`
- `com/jy.smali`
- `com/jz.smali`
- `com/k.smali`
- `com/kA.smali`
- `com/kB.smali`
- `com/kC.smali`
- `com/kD.smali`
- `com/kE.smali`
- `com/kF.smali`
- `com/kG.smali`
- `com/kH.smali`
- `com/kI.smali`
- `com/kJ.smali`
- `com/kK.smali`
- `com/kL.smali`
- `com/kM.smali`
- `com/kN.smali`
- `com/kO.smali`
- `com/kP.smali`
- `com/kQ.smali`
- `com/kR.smali`
- `com/kS.smali`
- `com/kT.smali`
- `com/kU.smali`
- `com/kV.smali`
- `com/kW.smali`
- `com/kX.smali`
- `com/kY.smali`
- `com/kZ.smali`
- `com/ka.smali`
- `com/kb.smali`
- `com/kc.smali`
- `com/kd.smali`
- `com/ke.smali`
- `com/kf.smali`
- `com/kg.smali`
- `com/kh.smali`
- `com/ki.smali`
- `com/kj.smali`
- `com/kk.smali`
- `com/kl.smali`
- `com/km.smali`
- `com/kn.smali`
- `com/ko.smali`
- `com/kp.smali`
- `com/kq.smali`
- `com/kr.smali`
- `com/ks.smali`
- `com/kt.smali`
- `com/ku.smali`
- `com/kv.smali`
- `com/kw.smali`
- `com/kx.smali`
- `com/ky.smali`
- `com/kz.smali`
- `com/l.smali`
- `com/lA.smali`
- `com/lB.smali`
- `com/lC.smali`
- `com/lD.smali`
- `com/lE.smali`
- `com/lF.smali`
- `com/lG.smali`
- `com/lH.smali`
- `com/lI.smali`
- `com/lJ.smali`
- `com/lK.smali`
- `com/lL.smali`
- `com/lM.smali`
- `com/lN.smali`
- `com/lO.smali`
- `com/lP.smali`
- `com/lQ.smali`
- `com/lR.smali`
- `com/lS.smali`
- `com/lT.smali`
- `com/lU.smali`
- `com/lV.smali`
- `com/lW.smali`
- `com/lX.smali`
- `com/lY.smali`
- `com/lZ.smali`
- `com/la.smali`
- `com/lb.smali`
- `com/lc.smali`
- `com/ld.smali`
- `com/le.smali`
- `com/lf.smali`
- `com/lg.smali`
- `com/lh.smali`
- `com/li.smali`
- `com/lj.smali`
- `com/lk.smali`
- `com/ll.smali`
- `com/lm.smali`
- `com/ln.smali`
- `com/lo.smali`
- `com/lp.smali`
- `com/lq.smali`
- `com/lr.smali`
- `com/ls.smali`
- `com/lt.smali`
- `com/lu.smali`
- `com/lv.smali`
- `com/lw.smali`
- `com/lx.smali`
- `com/ly.smali`
- `com/lz.smali`
- `com/m.smali`
- `com/mA.smali`
- `com/mB.smali`
- `com/mC.smali`
- `com/mD.smali`
- `com/mE.smali`
- `com/mF.smali`
- `com/mG.smali`
- `com/mH.smali`
- `com/mI.smali`
- `com/mJ.smali`
- `com/mK.smali`
- `com/mL.smali`
- `com/mM.smali`
- `com/mN.smali`
- `com/mO.smali`
- `com/mP.smali`
- `com/mQ.smali`
- `com/mR.smali`
- `com/mS.smali`
- `com/mT.smali`
- `com/mU.smali`
- `com/mV.smali`
- `com/mW.smali`
- `com/mX.smali`
- `com/mY.smali`
- `com/mZ.smali`
- `com/ma.smali`
- `com/mb.smali`
- `com/mc.smali`
- `com/md.smali`
- `com/me.smali`
- `com/mf.smali`
- `com/mg.smali`
- `com/mh.smali`
- `com/mi.smali`
- `com/mj.smali`
- `com/mk.smali`
- `com/ml.smali`
- `com/mm.smali`
- `com/mn.smali`
- `com/mo.smali`
- `com/mp.smali`
- `com/mq.smali`
- `com/mr.smali`
- `com/ms.smali`
- `com/mt.smali`
- `com/mu.smali`
- `com/mv.smali`
- `com/mw.smali`
- `com/mx.smali`
- `com/my.smali`
- `com/mz.smali`
- `com/n.smali`
- `com/nA.smali`
- `com/nB.smali`
- `com/nC.smali`
- `com/nD.smali`
- `com/nE.smali`
- `com/nF.smali`
- `com/nG.smali`
- `com/nH.smali`
- `com/nI.smali`
- `com/nJ.smali`
- `com/nK.smali`
- `com/nL.smali`
- `com/nM.smali`
- `com/nN.smali`
- `com/nO.smali`
- `com/nP.smali`
- `com/nQ.smali`
- `com/nR.smali`
- `com/nS.smali`
- `com/nT.smali`
- `com/nU.smali`
- `com/nV.smali`
- `com/nW.smali`
- `com/nX.smali`
- `com/nY.smali`
- `com/nZ.smali`
- `com/na.smali`
- `com/nb.smali`
- `com/nc.smali`
- `com/nd.smali`
- `com/ne.smali`
- `com/nf.smali`
- `com/ng.smali`
- `com/nh.smali`
- `com/ni.smali`
- `com/nj.smali`
- `com/nk.smali`
- `com/nl.smali`
- `com/nm.smali`
- `com/nn.smali`
- `com/no.smali`
- `com/np.smali`
- `com/nq.smali`
- `com/nr.smali`
- `com/ns.smali`
- `com/nt.smali`
- `com/nu.smali`
- `com/nv.smali`
- `com/nw.smali`
- `com/nx.smali`
- `com/ny.smali`
- `com/nz.smali`
- `com/o.smali`
- `com/oA.smali`
- `com/oB.smali`
- `com/oC.smali`
- `com/oD.smali`
- `com/oE.smali`
- `com/oF.smali`
- `com/oG.smali`
- `com/oH.smali`
- `com/oI.smali`
- `com/oJ.smali`
- `com/oK.smali`
- `com/oL.smali`
- `com/oM.smali`
- `com/oN.smali`
- `com/oO.smali`
- `com/oP.smali`
- `com/oQ.smali`
- `com/oR.smali`
- `com/oS.smali`
- `com/oT.smali`
- `com/oU.smali`
- `com/oV.smali`
- `com/oW.smali`
- `com/oX.smali`
- `com/oY.smali`
- `com/oZ.smali`
- `com/oa.smali`
- `com/ob.smali`
- `com/oc.smali`
- `com/od.smali`
- `com/oe.smali`
- `com/of.smali`
- `com/og.smali`
- `com/oh.smali`
- `com/oi.smali`
- `com/oj.smali`
- `com/ok.smali`
- `com/ol.smali`
- `com/om.smali`
- `com/on.smali`
- `com/oo.smali`
- `com/op.smali`
- `com/oq.smali`
- `com/or.smali`
- `com/os.smali`
- `com/ot.smali`
- `com/ou.smali`
- `com/ov.smali`
- `com/ow.smali`
- `com/ox.smali`
- `com/oy.smali`
- `com/oz.smali`
- `com/p.smali`
- `com/pA.smali`
- `com/pB.smali`
- `com/pC.smali`
- `com/pD.smali`
- `com/pE.smali`
- `com/pF.smali`
- `com/pG.smali`
- `com/pH.smali`
- `com/pI.smali`
- `com/pJ.smali`
- `com/pK.smali`
- `com/pL.smali`
- `com/pM.smali`
- `com/pN.smali`
- `com/pO.smali`
- `com/pP.smali`
- `com/pQ.smali`
- `com/pR.smali`
- `com/pS.smali`
- `com/pT.smali`
- `com/pU.smali`
- `com/pV.smali`
- `com/pW.smali`
- `com/pX.smali`
- `com/pY.smali`
- `com/pZ.smali`
- `com/pa.smali`
- `com/pb.smali`
- `com/pc.smali`
- `com/pd.smali`
- `com/pe.smali`
- `com/pf.smali`
- `com/pg.smali`
- `com/ph.smali`
- `com/pi.smali`
- `com/pj.smali`
- `com/pk.smali`
- `com/pl.smali`
- `com/pm.smali`
- `com/pn.smali`
- `com/po.smali`
- `com/pp.smali`
- `com/pq.smali`
- `com/pr.smali`
- `com/ps.smali`
- `com/pt.smali`
- `com/pu.smali`
- `com/pv.smali`
- `com/pw.smali`
- `com/px.smali`
- `com/py.smali`
- `com/pz.smali`
- `com/q.smali`
- `com/qA.smali`
- `com/qB.smali`
- `com/qC.smali`
- `com/qD.smali`
- `com/qE.smali`
- `com/qF.smali`
- `com/qG.smali`
- `com/qH.smali`
- `com/qI.smali`
- `com/qJ.smali`
- `com/qK.smali`
- `com/qL.smali`
- `com/qM.smali`
- `com/qN.smali`
- `com/qO.smali`
- `com/qP.smali`
- `com/qQ.smali`
- `com/qR.smali`
- `com/qS.smali`
- `com/qT.smali`
- `com/qU.smali`
- `com/qV.smali`
- `com/qW.smali`
- `com/qX.smali`
- `com/qY.smali`
- `com/qZ.smali`
- `com/qa.smali`
- `com/qb.smali`
- `com/qc.smali`
- `com/qd.smali`
- `com/qe.smali`
- `com/qf.smali`
- `com/qg.smali`
- `com/qh.smali`
- `com/qi.smali`
- `com/qj.smali`
- `com/qk.smali`
- `com/ql.smali`
- `com/qm.smali`
- `com/qn.smali`
- `com/qo.smali`
- `com/qp.smali`
- `com/qq.smali`
- `com/qr.smali`
- `com/qs.smali`
- `com/qt.smali`
- `com/qu.smali`
- `com/qv.smali`
- `com/qw.smali`
- `com/qx.smali`
- `com/qy.smali`
- `com/qz.smali`
- `com/r.smali`
- `com/rA.smali`
- `com/rB.smali`
- `com/rC.smali`
- `com/rD.smali`
- `com/rE.smali`
- `com/rF.smali`
- `com/rG.smali`
- `com/rH.smali`
- `com/rI.smali`
- `com/rJ.smali`
- `com/rK.smali`
- `com/rL.smali`
- `com/rM.smali`
- `com/rN.smali`
- `com/rO.smali`
- `com/rP.smali`
- `com/rQ.smali`
- `com/rR.smali`
- `com/rS.smali`
- `com/rT.smali`
- `com/rU.smali`
- `com/rV.smali`
- `com/rW.smali`
- `com/rX.smali`
- `com/rY.smali`
- `com/rZ.smali`
- `com/ra.smali`
- `com/rb.smali`
- `com/rc.smali`
- `com/rd.smali`
- `com/re.smali`
- `com/rf.smali`
- `com/rg.smali`
- `com/rh.smali`
- `com/ri.smali`
- `com/rj.smali`
- `com/rk.smali`
- `com/rl.smali`
- `com/rm.smali`
- `com/rn.smali`
- `com/ro.smali`
- `com/rp.smali`
- `com/rq.smali`
- `com/rr.smali`
- `com/rs.smali`
- `com/rt.smali`
- `com/ru.smali`
- `com/rv.smali`
- `com/rw.smali`
- `com/rx.smali`
- `com/ry.smali`
- `com/rz.smali`
- `com/s.smali`
- `com/sA.smali`
- `com/sB.smali`
- `com/sC.smali`
- `com/sD.smali`
- `com/sE.smali`
- `com/sF.smali`
- `com/sG.smali`
- `com/sH.smali`
- `com/sI.smali`
- `com/sJ.smali`
- `com/sK.smali`
- `com/sL.smali`
- `com/sM.smali`
- `com/sN.smali`
- `com/sO.smali`
- `com/sP.smali`
- `com/sQ.smali`
- `com/sR.smali`
- `com/sS.smali`
- `com/sT.smali`
- `com/sU.smali`
- `com/sV.smali`
- `com/sW.smali`
- `com/sX.smali`
- `com/sY.smali`
- `com/sZ.smali`
- `com/sa.smali`
- `com/sb.smali`
- `com/sc.smali`
- `com/sd.smali`
- `com/se.smali`
- `com/sf.smali`
- `com/sg.smali`
- `com/sh.smali`
- `com/si.smali`
- `com/sj.smali`
- `com/sk.smali`
- `com/sl.smali`
- `com/sm.smali`
- `com/sn.smali`
- `com/so.smali`
- `com/sp.smali`
- `com/sq.smali`
- `com/sr.smali`
- `com/ss.smali`
- `com/st.smali`
- `com/su.smali`
- `com/sv.smali`
- `com/sw.smali`
- `com/sx.smali`
- `com/sy.smali`
- `com/sz.smali`
- `com/t.smali`
- `com/tA.smali`
- `com/tB.smali`
- `com/tC.smali`
- `com/tD.smali`
- `com/tE.smali`
- `com/tF.smali`
- `com/tG.smali`
- `com/tH.smali`
- `com/tI.smali`
- `com/tJ.smali`
- `com/tK.smali`
- `com/tL.smali`
- `com/tM.smali`
- `com/tN.smali`
- `com/tO.smali`
- `com/tP.smali`
- `com/tQ.smali`
- `com/tR.smali`
- `com/tS.smali`
- `com/tT.smali`
- `com/tU.smali`
- `com/tV.smali`
- `com/tW.smali`
- `com/tX.smali`
- `com/tY.smali`
- `com/ta.smali`
- `com/tb.smali`
- `com/tc.smali`
- `com/td.smali`
- `com/te.smali`
- `com/tf.smali`
- `com/tg.smali`
- `com/th.smali`
- `com/ti.smali`
- `com/tj.smali`
- `com/tk.smali`
- `com/tl.smali`
- `com/tm.smali`
- `com/tn.smali`
- `com/to.smali`
- `com/tp.smali`
- `com/tq.smali`
- `com/tr.smali`
- `com/ts.smali`
- `com/tt.smali`
- `com/tu.smali`
- `com/tv.smali`
- `com/tw.smali`
- `com/tx.smali`
- `com/ty.smali`
- `com/tz.smali`
- `com/u.smali`
- `com/v.smali`
- `com/w.smali`
- `com/x.smali`
- `com/y.smali`
- `com/z.smali`

### `com/dragon/` — 77 类
- `com/dragon/read/ad/util/۟ۢۢۤۤ.smali`
- `com/dragon/read/ad/util/۟ۥۡۤۧ.smali`
- `com/dragon/read/ad/util/۠۟ۦۤ.smali`
- `com/dragon/read/ad/util/۠ۥۣ۟.smali`
- `com/dragon/read/ad/util/ۡ۟ۤۢ.smali`
- `com/dragon/read/ad/util/ۢۥۥۥ.smali`
- `com/dragon/read/ad/util/ۢۧۦۦ.smali`
- `com/dragon/read/ad/util/ۣۢۨۢ.smali`
- `com/dragon/read/ad/util/ۦۨ۠ۥ.smali`
- `com/dragon/read/ad/util/ۧۤ۠۠.smali`
- `com/dragon/read/ad/util/ۧۦۤۤ.smali`
- `com/dragon/read/base/ssconfig/model/۟۠ۨۨ۟.smali`
- `com/dragon/read/base/ssconfig/model/۟ۡ۠ۧۢ.smali`
- `com/dragon/read/base/ssconfig/model/ۣۣ۟۠۟.smali`
- `com/dragon/read/base/ssconfig/model/ۣۣ۟ۤۨ.smali`
- `com/dragon/read/base/ssconfig/model/۟ۦۤ۠۟.smali`
- `com/dragon/read/base/ssconfig/model/ۤۨ۟۠.smali`
- `com/dragon/read/base/ssconfig/model/ۥۦۥۦ.smali`
- `com/dragon/read/base/ssconfig/model/ۦۤۨۦ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/ۣ۟۠۠ۨ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/۟ۤۡۨ۟.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/۠ۢۦ۠.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/ۢۥۡ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/ۣۤۨ۟.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۣ۟ۢ۟.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۣ۟ۤۦۧ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/۠۠ۥۡ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/۠ۥۡۡ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۢ۟ۦ۟.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۢۥۦۨ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۣۨ.smali`
- `com/dragon/read/component/biz/impl/mine/۠ۡ.smali`
- `com/dragon/read/pages/main/ۣ۟ۡۥۤ.smali`
- `com/dragon/read/pages/main/۟ۧۦ۟ۥ.smali`
- `com/dragon/read/pages/main/ۤۢۨ.smali`
- `com/dragon/read/pages/main/ۣۤۤۨ.smali`
- `com/dragon/read/pages/main/ۤۦ۟ۡ.smali`
- `com/dragon/read/pages/main/ۤۦۦۧ.smali`
- `com/dragon/read/pages/main/ۧۨۦۦ.smali`
- `com/dragon/read/polaris/۟ۡ۠ۢۧ.smali`
- `com/dragon/read/polaris/۟ۢۦۦ.smali`
- `com/dragon/read/polaris/۟ۧۢۥۨ.smali`
- `com/dragon/read/polaris/ۡ۟ۢۡ.smali`
- `com/dragon/read/polaris/ۣۢۧۨ.smali`
- `com/dragon/read/polaris/ۤۥ۠ۨ.smali`
- `com/dragon/read/polaris/ۧ۟ۡ۠.smali`
- `com/dragon/read/polaris/ۨ۟۟ۡ.smali`
- `com/dragon/read/reader/ad/noad/۟ۥۣۡۦ.smali`
- `com/dragon/read/reader/ad/noad/۟ۧۡۧۤ.smali`
- `com/dragon/read/reader/ad/noad/۟ۧۤۦۢ.smali`
- `com/dragon/read/reader/ad/noad/ۡۦۧۡ.smali`
- `com/dragon/read/reader/ad/noad/ۣۣۤۨ.smali`
- `com/dragon/read/reader/ad/noad/ۦۢ۟ۡ.smali`
- `com/dragon/read/reader/ad/۟ۡ۠ۧ۟.smali`
- `com/dragon/read/reader/ad/۟ۤۡۢ۟.smali`
- `com/dragon/read/reader/ad/ۡۡۤ۟.smali`
- `com/dragon/read/reader/ad/ۣ۟ۦ۟.smali`
- `com/dragon/read/reader/ad/ۥۢۨۡ.smali`
- `com/dragon/read/reader/ad/ۧ۟۟ۦ.smali`
- `com/dragon/read/reader/ad/ۣۨۢۧ.smali`
- `com/dragon/read/rpc/rpc/۟۟ۥۢ۠.smali`
- `com/dragon/read/rpc/rpc/۟ۧۡ۠ۦ.smali`
- `com/dragon/read/rpc/rpc/ۣۥۢۡ.smali`
- `com/dragon/read/user/model/۟۠۟۟ۡ.smali`
- `com/dragon/read/user/model/۟۠ۤۧ۠.smali`
- `com/dragon/read/user/model/۟ۡ۟۟ۨ.smali`
- `com/dragon/read/user/model/۟ۢۦۥۨ.smali`
- `com/dragon/read/user/model/۟ۧۤ۠ۤ.smali`
- `com/dragon/read/user/model/۟ۧۦۦۦ.smali`
- `com/dragon/read/user/model/ۣ۟ۥ۠.smali`
- `com/dragon/read/user/model/ۤۢۢۧ.smali`
- `com/dragon/read/util/۟۟۟ۧ۟.smali`
- `com/dragon/read/util/ۣ۟ۢۢ۟.smali`
- `com/dragon/read/util/ۣ۟ۤ۟ۧ.smali`
- `com/dragon/read/util/۠ۤۦ۠.smali`
- `com/dragon/read/util/ۢۡ۟ۦ.smali`
- `com/dragon/read/util/ۥ۠ۧۢ.smali`

### `org/checkerframework/` — 34 类
- `org/checkerframework/checker/signature/query/security/̅.smali`
- `org/checkerframework/checker/signature/query/security/̍.smali`
- `org/checkerframework/checker/signature/query/security/̎.smali`
- `org/checkerframework/checker/signature/query/security/̐.smali`
- `org/checkerframework/checker/signature/query/security/̒.smali`
- `org/checkerframework/checker/signature/query/security/̓.smali`
- `org/checkerframework/checker/signature/query/security/̔.smali`
- `org/checkerframework/checker/signature/query/security/̕.smali`
- `org/checkerframework/checker/signature/query/security/̖.smali`
- `org/checkerframework/checker/signature/query/security/̗.smali`
- `org/checkerframework/checker/signature/query/security/̘.smali`
- `org/checkerframework/checker/signature/query/security/̙.smali`
- `org/checkerframework/checker/signature/query/security/̚.smali`
- `org/checkerframework/checker/signature/query/security/̜.smali`
- `org/checkerframework/checker/signature/query/security/̝.smali`
- `org/checkerframework/checker/signature/query/security/̞.smali`
- `org/checkerframework/checker/signature/query/security/̟.smali`
- `org/checkerframework/checker/signature/query/security/̠.smali`
- `org/checkerframework/checker/signature/query/security/̡.smali`
- `org/checkerframework/checker/signature/query/security/̢.smali`
- `org/checkerframework/checker/signature/query/security/̩.smali`
- `org/checkerframework/checker/signature/query/security/̪.smali`
- `org/checkerframework/checker/signature/query/security/̫.smali`
- `org/checkerframework/checker/signature/query/security/̬.smali`
- `org/checkerframework/checker/signature/query/security/̯.smali`
- `org/checkerframework/checker/signature/query/security/̲.smali`
- `org/checkerframework/checker/signature/query/security/̳.smali`
- `org/checkerframework/checker/signature/query/security/а$ClipRoundLayout.smali`
- `org/checkerframework/checker/signature/query/security/а.smali`
- `org/checkerframework/checker/signature/query/security/۟۠ۥۨۦ.smali`
- `org/checkerframework/checker/signature/query/security/ۣ۟ۥۡ.smali`
- `org/checkerframework/checker/signature/query/security/ۣۢۨ۠.smali`
- `org/checkerframework/checker/signature/query/security/ۤ۟ۥ.smali`
- `org/checkerframework/checker/signature/query/security/ۨۢۥۧ.smali`

### `org/lsposed/` — 12 类
- `org/lsposed/hiddenapibypass/CoreOjClassLoader.smali`
- `org/lsposed/hiddenapibypass/Helper$AccessibleObject.smali`
- `org/lsposed/hiddenapibypass/Helper$Class.smali`
- `org/lsposed/hiddenapibypass/Helper$Executable.smali`
- `org/lsposed/hiddenapibypass/Helper$InvokeStub.smali`
- `org/lsposed/hiddenapibypass/Helper$MethodHandle.smali`
- `org/lsposed/hiddenapibypass/Helper$NeverCall.smali`
- `org/lsposed/hiddenapibypass/Helper.smali`
- `org/lsposed/hiddenapibypass/HiddenApiBypass.smali`
- `org/lsposed/hiddenapibypass/LSPass.smali`
- `org/lsposed/hiddenapibypass/library/BuildConfig.smali`
- `org/lsposed/hiddenapibypass/library/R.smali`

### `an2/` — 9 类
- `an2/۟ۡۧۤۧ.smali`
- `an2/۟ۢۢ۠ۦ.smali`
- `an2/۟ۦۧۤ۟.smali`
- `an2/۟ۦۨۢۤ.smali`
- `an2/ۡۥ۠ۦ.smali`
- `an2/ۥۣۣۢ.smali`
- `an2/ۦۥۣ.smali`
- `an2/ۧۢۧ۠.smali`
- `an2/ۧۥۥۤ.smali`

### `com/pandora/` — 7 类
- `com/pandora/core/AppFactory$DATA.smali`
- `com/pandora/core/AppFactory.smali`
- `com/pandora/core/Copyright.smali`
- `com/pandora/core/CreatorProxy.smali`
- `com/pandora/core/۟۠ۥۧ۟.smali`
- `com/pandora/core/ۣ۟ۢۢۡ.smali`
- `com/pandora/core/ۣۥۨۤ.smali`

### `com/b/` — 3 类
- `com/b/a$Android_id.smali`
- `com/b/a$Reflect.smali`
- `com/b/a.smali`

### `com/ss/` — 2 类
- `com/ss/android/update/ۡ۠ۥۥ.smali`
- `com/ss/android/update/ۣۨ۟.smali`

### `sgcore0/` — 1 类
- `sgcore0/SafeLoader.smali`

### `sgcore0/hidden/` — 1 类
- `sgcore0/hidden/Hidden0.smali`

## 3. 修改类清单（按差异方法总数降序）

| 类 | +新增 | -删除 | ~修改 | 合计 |
|---|---|---|---|---|
| `com/dragon/read/pages/main/MainFragmentActivity.smali` | 1039 | 0 | 133 | 1172 |
| `com/dragon/read/util/DebugManager.smali` | 70 | 0 | 506 | 576 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2.smali` | 415 | 0 | 63 | 478 |
| `com/dragon/read/rpc/rpc/UgcApiService.smali` | 203 | 0 | 203 | 406 |
| `com/dragon/read/rpc/rpc/UserApiService.smali` | 179 | 0 | 179 | 358 |
| `com/dragon/read/reader/ad/ReaderAdManager.smali` | 299 | 0 | 35 | 334 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment.smali` | 189 | 0 | 41 | 230 |
| `com/dragon/read/pages/main/k2.smali` | 212 | 0 | 2 | 214 |
| `com/dragon/read/util/ImageLoaderUtils.smali` | 111 | 0 | 72 | 183 |
| `com/dragon/read/util/j4.smali` | 159 | 0 | 12 | 171 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment.smali` | 154 | 0 | 14 | 168 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment.smali` | 120 | 0 | 39 | 159 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2.smali` | 139 | 0 | 18 | 157 |
| `com/dragon/read/util/ApkSizeOptImageLoader.smali` | 131 | 0 | 9 | 140 |
| `com/dragon/read/util/j.smali` | 113 | 0 | 26 | 139 |
| `com/dragon/read/util/BookUtils.smali` | 56 | 0 | 77 | 133 |
| `com/ss/android/update/z.smali` | 66 | 24 | 42 | 132 |
| `com/dragon/read/ad/util/AdUtil.smali` | 115 | 0 | 10 | 125 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment.smali` | 88 | 0 | 28 | 116 |
| `com/ss/videoarch/liveplayer/VideoLiveManager.smali` | 0 | 0 | 116 | 116 |
| `com/dragon/read/pages/main/MainFragmentActivity$b0.smali` | 113 | 0 | 2 | 115 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard.smali` | 93 | 0 | 15 | 108 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment.smali` | 91 | 0 | 13 | 104 |
| `com/dragon/read/util/p8.smali` | 92 | 0 | 8 | 100 |
| `com/dragon/read/pages/main/k4.smali` | 71 | 1 | 21 | 93 |
| `an2/x0.smali` | 80 | 0 | 11 | 91 |
| `com/dragon/read/util/ToastUtils.smali` | 35 | 0 | 54 | 89 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment.smali` | 63 | 0 | 21 | 84 |
| `com/dragon/read/util/PictureUtils.smali` | 48 | 0 | 34 | 82 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity.smali` | 68 | 0 | 13 | 81 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineConfigImpl.smali` | 54 | 0 | 22 | 76 |
| `com/dragon/read/pages/main/w2.smali` | 70 | 0 | 5 | 75 |
| `com/ss/videoarch/liveplayer/log/LiveLoggerService.smali` | 0 | 0 | 74 | 74 |
| `com/dragon/read/pages/main/MainPageDrawerLayout.smali` | 7 | 0 | 61 | 68 |
| `com/ss/android/update/UpdateServiceImpl.smali` | 10 | 0 | 56 | 66 |
| `com/dragon/read/ad/util/u0.smali` | 42 | 0 | 22 | 64 |
| `com/ss/ttvideoengine/TTVideoEngineImpl.smali` | 0 | 0 | 64 | 64 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner.smali` | 0 | 0 | 63 | 63 |
| `com/dragon/read/util/BitmapUtils.smali` | 21 | 0 | 42 | 63 |
| `com/dragon/read/ad/util/c0.smali` | 55 | 0 | 7 | 62 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil.smali` | 54 | 0 | 7 | 61 |
| `com/dragon/read/pages/main/m.smali` | 57 | 0 | 4 | 61 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment.smali` | 36 | 0 | 24 | 60 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity.smali` | 48 | 0 | 10 | 58 |
| `com/dragon/read/util/l2.smali` | 48 | 0 | 9 | 57 |
| `com/dragon/read/reader/ad/AdLine.smali` | 42 | 0 | 14 | 56 |
| `com/dragon/read/util/CdnLargeImageLoader.smali` | 40 | 0 | 16 | 56 |
| `com/dragon/read/util/j1.smali` | 24 | 0 | 32 | 56 |
| `com/dragon/read/component/biz/impl/mine/NewAboutActivity.smali` | 45 | 0 | 10 | 55 |
| `com/dragon/read/util/AbiUtil.smali` | 33 | 0 | 22 | 55 |
| `com/dragon/read/component/biz/impl/mine/la.smali` | 52 | 0 | 2 | 54 |
| `com/dragon/read/util/UiUtils.smali` | 6 | 0 | 48 | 54 |
| `com/dragon/read/util/t0.smali` | 43 | 0 | 11 | 54 |
| `com/dragon/read/ad/util/a1.smali` | 42 | 0 | 9 | 51 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberNormalView.smali` | 36 | 0 | 15 | 51 |
| `com/dragon/read/pages/main/MainFragmentActivity$q.smali` | 49 | 0 | 2 | 51 |
| `com/dragon/read/util/RecentConsumeRecorder.smali` | 42 | 0 | 9 | 51 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/b.smali` | 43 | 0 | 7 | 50 |
| `com/dragon/read/pages/main/z.smali` | 40 | 0 | 10 | 50 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$g.smali` | 46 | 0 | 3 | 49 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberNormalViewForFullScreenVideo.smali` | 35 | 0 | 14 | 49 |
| `com/dragon/read/reader/ad/ReaderAdManager$a.smali` | 47 | 0 | 2 | 49 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity.smali` | 34 | 0 | 13 | 47 |
| `com/dragon/read/util/UiConfigSetter.smali` | 18 | 0 | 29 | 47 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/a.smali` | 39 | 0 | 7 | 46 |
| `com/dragon/read/util/FileUtils.smali` | 13 | 0 | 33 | 46 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2$a.smali` | 43 | 0 | 2 | 45 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$c.smali` | 32 | 0 | 12 | 44 |
| `com/dragon/read/rpc/rpc/MsgApiService.smali` | 22 | 0 | 22 | 44 |
| `com/dragon/read/util/h.smali` | 40 | 0 | 4 | 44 |
| `com/dragon/read/util/k.smali` | 32 | 0 | 12 | 44 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$b.smali` | 37 | 0 | 5 | 42 |
| `com/dragon/read/component/biz/impl/mine/o8.smali` | 40 | 0 | 2 | 42 |
| `com/dragon/read/util/p8$b.smali` | 37 | 0 | 5 | 42 |
| `com/dragon/read/ad/util/i0.smali` | 36 | 0 | 5 | 41 |
| `com/dragon/read/util/UriUtils.smali` | 19 | 0 | 22 | 41 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c.smali` | 32 | 0 | 8 | 40 |
| `com/dragon/read/pages/main/f5.smali` | 33 | 0 | 7 | 40 |
| `com/dragon/read/util/v.smali` | 36 | 0 | 4 | 40 |
| `an2/i0.smali` | 34 | 0 | 5 | 39 |
| `com/dragon/read/component/biz/impl/mine/of.smali` | 37 | 0 | 2 | 39 |
| `com/dragon/read/pages/main/r4.smali` | 28 | 0 | 11 | 39 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$Companion.smali` | 35 | 0 | 4 | 39 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog.smali` | 32 | 0 | 7 | 39 |
| `com/dragon/read/util/ReaderCommonColor.smali` | 8 | 0 | 31 | 39 |
| `com/dragon/read/component/biz/impl/mine/DiggContentActivity.smali` | 30 | 0 | 8 | 38 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$a.smali` | 36 | 0 | 2 | 38 |
| `com/dragon/read/pages/main/g.smali` | 29 | 0 | 9 | 38 |
| `com/dragon/read/reader/ad/a0.smali` | 28 | 1 | 8 | 37 |
| `com/dragon/read/reader/ad/h.smali` | 11 | 0 | 26 | 37 |
| `com/dragon/read/util/NetReqUtil.smali` | 25 | 0 | 12 | 37 |
| `com/dragon/read/util/d5.smali` | 27 | 0 | 10 | 37 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenLoginActivity.smali` | 20 | 0 | 16 | 36 |
| `com/dragon/read/user/model/PrivilegeInfoModel.smali` | 15 | 0 | 21 | 36 |
| `com/dragon/read/util/PremiumReportHelper.smali` | 18 | 0 | 18 | 36 |
| `com/dragon/read/pages/main/t4.smali` | 31 | 0 | 4 | 35 |
| `com/dragon/read/util/b4.smali` | 30 | 0 | 5 | 35 |
| `com/dragon/read/ad/util/k0.smali` | 20 | 0 | 14 | 34 |
| `com/dragon/read/component/biz/impl/mine/LoginActivity.smali` | 24 | 0 | 10 | 34 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment.smali` | 14 | 0 | 20 | 34 |
| `com/dragon/read/pages/main/q.smali` | 32 | 0 | 2 | 34 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/k.smali` | 29 | 0 | 4 | 33 |
| `com/dragon/read/component/biz/impl/mine/kd.smali` | 20 | 0 | 12 | 32 |
| `com/dragon/read/pages/main/IFixRefreshBottomTab$$Impl.smali` | 28 | 0 | 4 | 32 |
| `com/dragon/read/reader/ad/d.smali` | 24 | 0 | 8 | 32 |
| `com/ss/ttvideoengine/InfoWrapper.smali` | 0 | 0 | 32 | 32 |
| `com/bytedance/android/ad/sdk/init/BDASdkRuntimeInitConfig.smali` | 0 | 0 | 31 | 31 |
| `com/dragon/read/component/biz/impl/mine/MineBottomTabLandingGuideServiceImpl.smali` | 20 | 0 | 11 | 31 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/e.smali` | 23 | 0 | 8 | 31 |
| `com/dragon/read/util/b8.smali` | 6 | 0 | 25 | 31 |
| `com/dragon/read/util/g5.smali` | 24 | 0 | 7 | 31 |
| `com/dragon/read/util/k4.smali` | 25 | 0 | 6 | 31 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/i.smali` | 26 | 0 | 4 | 30 |
| `com/dragon/read/pages/main/MainFragmentActivity$d0.smali` | 27 | 0 | 3 | 30 |
| `com/dragon/read/reader/ad/c.smali` | 26 | 0 | 4 | 30 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/g.smali` | 0 | 0 | 29 | 29 |
| `com/dragon/read/ad/util/q0.smali` | 22 | 0 | 7 | 29 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenBindDouyinActivity.smali` | 17 | 0 | 12 | 29 |
| `com/dragon/read/pages/main/k.smali` | 25 | 0 | 4 | 29 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$h.smali` | 26 | 0 | 2 | 28 |
| `com/dragon/read/util/p0.smali` | 26 | 0 | 2 | 28 |
| `com/ss/android/update/UpdateProgressActivity.smali` | 10 | 0 | 18 | 28 |
| `com/dragon/read/component/biz/impl/mine/ai.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/component/biz/impl/mine/ub.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/pages/main/PermissionGuidanceDialogActivity.smali` | 18 | 0 | 9 | 27 |
| `com/dragon/read/pages/main/e.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/util/i0.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/util/j3.smali` | 25 | 0 | 2 | 27 |
| `an2/t.smali` | 20 | 0 | 6 | 26 |
| `com/dragon/read/ad/util/f.smali` | 20 | 0 | 6 | 26 |
| `com/dragon/read/ad/util/j.smali` | 24 | 0 | 2 | 26 |
| `com/dragon/read/component/biz/impl/mine/ce.smali` | 21 | 0 | 5 | 26 |
| `com/dragon/read/pages/main/MainFragmentActivity$r.smali` | 24 | 0 | 2 | 26 |
| `com/dragon/read/pages/main/l.smali` | 24 | 0 | 2 | 26 |
| `com/dragon/read/util/CustomFrescoMonitor.smali` | 19 | 0 | 7 | 26 |
| `com/dragon/read/component/biz/impl/mine/i8.smali` | 15 | 0 | 10 | 25 |
| `an2/c0.smali` | 20 | 0 | 4 | 24 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$h.smali` | 21 | 0 | 3 | 24 |
| `com/dragon/read/util/x7.smali` | 19 | 0 | 5 | 24 |
| `com/ss/android/update/z$b.smali` | 22 | 0 | 2 | 24 |
| `com/dragon/read/component/biz/impl/mine/BsMineFragmentFactory.smali` | 14 | 0 | 9 | 23 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$b.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/component/biz/impl/mine/dg.smali` | 18 | 0 | 5 | 23 |
| `com/dragon/read/pages/main/p.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/pages/main/p4.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/pages/main/w.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$a.smali` | 20 | 0 | 3 | 23 |
| `com/dragon/read/util/MeasureUtil.smali` | 9 | 0 | 14 | 23 |
| `com/dragon/read/util/PictureUtils$g.smali` | 20 | 0 | 3 | 23 |
| `com/dragon/read/util/u6.smali` | 19 | 0 | 4 | 23 |
| `com/ss/android/update/x.smali` | 5 | 0 | 18 | 23 |
| `com/dragon/read/component/biz/impl/mine/d9.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/component/biz/impl/mine/i.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/j.smali` | 18 | 0 | 4 | 22 |
| `com/dragon/read/component/biz/impl/mine/ph.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/util/NumberUtils.smali` | 3 | 0 | 19 | 22 |
| `com/dragon/read/util/g7.smali` | 10 | 0 | 12 | 22 |
| `com/dragon/read/util/r0.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/ad/util/r.smali` | 17 | 0 | 4 | 21 |
| `com/dragon/read/ad/util/s0.smali` | 18 | 0 | 3 | 21 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$e.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/component/biz/impl/mine/RapidLoginFragment.smali` | 14 | 0 | 7 | 21 |
| `com/dragon/read/component/biz/impl/mine/l.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/component/biz/impl/mine/oa.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/pages/main/n0.smali` | 18 | 0 | 3 | 21 |
| `com/dragon/read/pages/main/z$f.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/util/f2.smali` | 1 | 0 | 20 | 21 |
| `com/dragon/read/util/m1.smali` | 12 | 0 | 9 | 21 |
| `com/dragon/read/util/v5.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/util/x2.smali` | 17 | 0 | 4 | 21 |
| `com/ss/ttvideoengine/log/VideoEventLoggerV2.smali` | 0 | 0 | 21 | 21 |
| `an2/c.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/ad/util/e.smali` | 12 | 0 | 8 | 20 |
| `com/dragon/read/component/biz/impl/mine/c.smali` | 13 | 0 | 7 | 20 |
| `com/dragon/read/component/biz/impl/mine/pc.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/component/biz/impl/mine/xg.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/pages/main/j.smali` | 2 | 0 | 18 | 20 |
| `com/dragon/read/pages/main/j3.smali` | 7 | 0 | 13 | 20 |
| `com/dragon/read/util/f5.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/util/i4.smali` | 16 | 0 | 4 | 20 |
| `com/dragon/read/util/ib.smali` | 14 | 0 | 6 | 20 |
| `com/dragon/read/util/o6.smali` | 15 | 0 | 5 | 20 |
| `com/dragon/read/ad/util/g.smali` | 15 | 0 | 4 | 19 |
| `com/dragon/read/component/biz/impl/mine/k.smali` | 13 | 0 | 6 | 19 |
| `com/dragon/read/component/biz/impl/mine/wb.smali` | 17 | 0 | 2 | 19 |
| `com/dragon/read/component/biz/impl/mine/yh.smali` | 15 | 0 | 4 | 19 |
| `com/dragon/read/pages/main/b4.smali` | 14 | 0 | 5 | 19 |
| `com/dragon/read/pages/main/g4.smali` | 15 | 0 | 4 | 19 |
| `com/dragon/read/pages/main/x1.smali` | 17 | 0 | 2 | 19 |
| `com/dragon/read/reader/ad/OfflineDefaultAdLine.smali` | 12 | 0 | 7 | 19 |
| `com/dragon/read/reader/ad/ReaderAdManager$f.smali` | 17 | 0 | 2 | 19 |
| `com/dragon/read/util/qa.smali` | 13 | 0 | 6 | 19 |
| `com/ss/texturerender/VideoSurfaceTexture.smali` | 0 | 0 | 19 | 19 |
| `an2/w.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/ad/util/g1.smali` | 15 | 0 | 3 | 18 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentProvider.smali` | 10 | 0 | 8 | 18 |
| `com/dragon/read/component/biz/impl/mine/gi.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/component/biz/impl/mine/w.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/util/a2.smali` | 10 | 0 | 8 | 18 |
| `com/dragon/read/util/k5.smali` | 12 | 0 | 6 | 18 |
| `com/dragon/read/util/n4.smali` | 15 | 0 | 3 | 18 |
| `com/dragon/read/util/n6.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/util/r.smali` | 4 | 0 | 14 | 18 |
| `com/dragon/read/util/r7.smali` | 13 | 0 | 5 | 18 |
| `com/ss/android/update/v.smali` | 6 | 0 | 12 | 18 |
| `com/ss/ttvideoengine/DataLoaderHelper.smali` | 0 | 0 | 18 | 18 |
| `an2/j.smali` | 14 | 0 | 3 | 17 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0.smali` | 0 | 0 | 17 | 17 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$g.smali` | 11 | 0 | 6 | 17 |
| `com/dragon/read/component/biz/impl/mine/ag.smali` | 15 | 0 | 2 | 17 |
| `com/dragon/read/pages/main/MainFragmentActivity$a0.smali` | 16 | 0 | 1 | 17 |
| `com/dragon/read/pages/main/e3.smali` | 15 | 0 | 2 | 17 |
| `com/dragon/read/pages/main/h3.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/pages/main/r3.smali` | 13 | 0 | 4 | 17 |
| `com/dragon/read/pages/main/x0.smali` | 15 | 0 | 2 | 17 |
| `com/dragon/read/polaris/PolarisConfigCenter.smali` | 10 | 0 | 7 | 17 |
| `com/dragon/read/util/a0.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/util/ab.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/util/d6.smali` | 11 | 0 | 6 | 17 |
| `com/dragon/read/util/db.smali` | 14 | 0 | 3 | 17 |
| `com/ss/mediakit/medialoader/AVMDLDataLoader.smali` | 0 | 0 | 17 | 17 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtils.smali` | 0 | 0 | 16 | 16 |
| `com/dragon/read/ad/util/h0.smali` | 13 | 0 | 3 | 16 |
| `com/dragon/read/ad/util/i.smali` | 10 | 0 | 6 | 16 |
| `com/dragon/read/ad/util/j0.smali` | 11 | 0 | 5 | 16 |
| `com/dragon/read/component/biz/impl/mine/HongguoEntryActivity.smali` | 8 | 0 | 8 | 16 |
| `com/dragon/read/component/biz/impl/mine/zf.smali` | 14 | 0 | 2 | 16 |
| `com/dragon/read/pages/main/i.smali` | 9 | 0 | 7 | 16 |
| `com/dragon/read/pages/main/x3.smali` | 14 | 0 | 2 | 16 |
| `com/dragon/read/util/ImageViewExtKt.smali` | 7 | 0 | 9 | 16 |
| `com/dragon/read/util/m0.smali` | 12 | 0 | 4 | 16 |
| `com/dragon/read/util/t4.smali` | 12 | 0 | 4 | 16 |
| `com/ss/android/update/i.smali` | 8 | 0 | 8 | 16 |
| `com/ss/android/update/u.smali` | 7 | 0 | 9 | 16 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/c0.smali` | 0 | 0 | 15 | 15 |
| `com/dragon/read/ad/util/c1.smali` | 12 | 0 | 3 | 15 |
| `com/dragon/read/component/biz/impl/mine/BottomTabLandingGuideSelectionDialogLauncher$show$1$2$1.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$onCreate$1$2$1$2$1.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenBindDouyinFragment.smali` | 12 | 0 | 3 | 15 |
| `com/dragon/read/component/biz/impl/mine/HongguoKmpWatchPreferenceFragment$b.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment$a.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$initHonorListView$1.smali` | 11 | 0 | 4 | 15 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$o.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/h.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/h9.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/hi.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/q8.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/zh.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/b4$b.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/d0.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/q1.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/z$e.smali` | 14 | 0 | 1 | 15 |
| `com/dragon/read/reader/ad/k.smali` | 10 | 0 | 5 | 15 |
| `com/dragon/read/reader/ad/v.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/util/AudioUtil.smali` | 9 | 0 | 6 | 15 |
| `com/dragon/read/util/CdnImageCacheEventListener.smali` | 6 | 0 | 9 | 15 |
| `com/dragon/read/util/ImageLoaderUtils$a.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/util/e6.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/util/g0.smali` | 8 | 0 | 7 | 15 |
| `com/dragon/read/util/q5.smali` | 9 | 0 | 6 | 15 |
| `com/dragon/read/util/t.smali` | 10 | 0 | 5 | 15 |
| `com/dragon/read/util/z7.smali` | 7 | 0 | 8 | 15 |
| `com/ss/videoarch/liveplayer/lss/LSSStrategyController.smali` | 0 | 0 | 15 | 15 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager.smali` | 0 | 0 | 14 | 14 |
| `com/dragon/read/ad/util/z.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$d.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity$b.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/dh.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/ig.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/pg.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/sa.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/sh.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/u9.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/a.smali` | 9 | 0 | 5 | 14 |
| `com/dragon/read/pages/main/e5.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/i2.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/z$a.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/z$g.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/reader/ad/FrontAdLine.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/reader/ad/x.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/CommonUiFlow.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/util/ExtractColorHost.smali` | 9 | 0 | 5 | 14 |
| `com/dragon/read/util/ImageLoaderUtils$a$a.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/StringUtils.smali` | 2 | 0 | 12 | 14 |
| `com/dragon/read/util/UiConfigSetter$adjust$1.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/util/a1.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/c1.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/f.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/util/i3.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/k3.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/l1.smali` | 8 | 0 | 6 | 14 |
| `com/dragon/read/util/r$a.smali` | 2 | 0 | 12 | 14 |
| `com/dragon/read/util/s6.smali` | 7 | 0 | 7 | 14 |
| `com/dragon/read/util/ta.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/w3$a.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/z6.smali` | 6 | 0 | 8 | 14 |
| `an2/g0.smali` | 11 | 0 | 2 | 13 |
| `an2/k0.smali` | 11 | 0 | 2 | 13 |
| `an2/q.smali` | 11 | 0 | 2 | 13 |
| `an2/u0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$c.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/c0$a.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/c0$b.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/c0$c.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/c0$d.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/d.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$f.smali` | 9 | 0 | 4 | 13 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$f.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$e.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/bh.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/df.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/fc.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/v8.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/w9.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/wg.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/yf.smali` | 6 | 0 | 7 | 13 |
| `com/dragon/read/pages/main/MainFragmentActivity$s.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/MiraCastMonitor.smali` | 9 | 0 | 4 | 13 |
| `com/dragon/read/pages/main/g0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/h0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/i3.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/pages/main/k1.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/v2.smali` | 5 | 0 | 8 | 13 |
| `com/dragon/read/util/CoroutineExecutor$execute$1.smali` | 9 | 0 | 4 | 13 |
| `com/dragon/read/util/FrequencyMgr.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/util/ImageLoaderUtils$u$a.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/util/c2.smali` | 6 | 0 | 7 | 13 |
| `com/dragon/read/util/c3.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/util/d0.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/util/d7.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/util/g1.smali` | 6 | 0 | 7 | 13 |
| `com/dragon/read/util/h0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/util/i.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/util/ib$a.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/util/r2.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/util/x3.smali` | 10 | 0 | 3 | 13 |
| `com/ss/android/update/q.smali` | 6 | 0 | 7 | 13 |
| `com/ss/texturerender/VideoTextureRenderer.smali` | 0 | 0 | 13 | 13 |
| `z50/b.smali` | 0 | 0 | 13 | 13 |
| `zb/b.smali` | 0 | 0 | 13 | 13 |
| `an2/b.smali` | 10 | 0 | 2 | 12 |
| `an2/b0.smali` | 10 | 0 | 2 | 12 |
| `an2/e0.smali` | 10 | 0 | 2 | 12 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment.smali` | 0 | 0 | 12 | 12 |
| `com/android/ttcjpaysdk/verify/utils/j.smali` | 0 | 0 | 12 | 12 |
| `com/dragon/read/ad/util/n.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$b.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/HongguoKmpWatchPreferenceFragment$a.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/HongguoKmpWatchPreferenceFragment.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineTabUIConfig.smali` | 3 | 0 | 9 | 12 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$q.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$o.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$e.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$a.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$i.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity$c.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$a.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$c.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/bd.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/ch.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/fg.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/hd.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/if.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/lg.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/LoginTypeView.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/component/biz/impl/mine/nc.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/qb.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/rf.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/sg.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/vb.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/vg.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/x.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/xb.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/yb.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/MainFragmentActivity$f.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/a4.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/m4.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/z4.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/reader/ad/ReaderAdManager$l.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/reader/ad/i.smali` | 5 | 0 | 7 | 12 |
| `com/dragon/read/reader/ad/s.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/util/FileProviderUtils.smali` | 8 | 0 | 4 | 12 |
| `com/dragon/read/util/ImageLoadHost.smali` | 8 | 0 | 4 | 12 |
| `com/dragon/read/util/ImageLoaderUtils$u.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/util/UiConfigSetter$h.smali` | 4 | 0 | 8 | 12 |
| `com/dragon/read/util/UiConfigSetter$i.smali` | 4 | 0 | 8 | 12 |
| `com/dragon/read/util/UiConfigSetter$n.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/util/e0$a.smali` | 11 | 0 | 1 | 12 |
| `com/dragon/read/util/f4.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/util/j7.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/util/l0.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/util/w7.smali` | 5 | 0 | 7 | 12 |
| `com/dragon/read/util/x4.smali` | 6 | 0 | 6 | 12 |
| `u9/a.smali` | 0 | 0 | 12 | 12 |
| `an2/a0.smali` | 9 | 0 | 2 | 11 |
| `an2/n.smali` | 9 | 0 | 2 | 11 |
| `an2/r.smali` | 9 | 0 | 2 | 11 |
| `an2/y.smali` | 8 | 0 | 3 | 11 |
| `an2/z.smali` | 8 | 0 | 3 | 11 |
| `an2/z0.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$a.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$h.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$l.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$k.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/bf.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/ce$a.smali` | 8 | 0 | 3 | 11 |
| `com/dragon/read/component/biz/impl/mine/d.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/component/biz/impl/mine/ei.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/ia.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/LoginTypeView$a.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/component/biz/impl/mine/o.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/qg.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/tg.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/y8.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/d5.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/f2.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/m2.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/pages/main/v.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/y1.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/user/model/NetIdLoginResp.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/ImageLoaderUtils$r.smali` | 8 | 0 | 3 | 11 |
| `com/dragon/read/util/OOMScoreAdjUtil.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/UiConfigSetter$b.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/UiConfigSetter$k.smali` | 4 | 0 | 7 | 11 |
| `com/dragon/read/util/b5.smali` | 8 | 0 | 3 | 11 |
| `com/dragon/read/util/b6.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/b7.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/e1.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/e5.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/f1.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/f8.smali` | 4 | 0 | 7 | 11 |
| `com/dragon/read/util/h$a.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/n2.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/p1.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/s7.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/u4.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/x0.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/x1.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/y0.smali` | 6 | 0 | 5 | 11 |
| `com/ss/android/update/t.smali` | 5 | 0 | 6 | 11 |
| `com/ss/ttvideoengine/TTVideoEngine.smali` | 0 | 0 | 11 | 11 |
| `com/ss/videoarch/liveplayer/PreloadHelper.smali` | 0 | 0 | 11 | 11 |
| `f9/c.smali` | 0 | 0 | 11 | 11 |
| `an2/f.smali` | 8 | 0 | 2 | 10 |
| `an2/g.smali` | 8 | 0 | 2 | 10 |
| `an2/p.smali` | 8 | 0 | 2 | 10 |
| `com/bytedance/alliance/utils/g.smali` | 0 | 0 | 10 | 10 |
| `com/dragon/read/ad/util/a0.smali` | 7 | 0 | 3 | 10 |
| `com/dragon/read/ad/util/x0.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$f.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$c.smali` | 9 | 0 | 1 | 10 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$k.smali` | 5 | 0 | 5 | 10 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$l.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$p.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$m.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2$c.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/bc.smali` | 7 | 0 | 3 | 10 |
| `com/dragon/read/component/biz/impl/mine/bi.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/eh.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/ga.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/ha.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/m9.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/r8.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/re.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/vh.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/yg.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/zg.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/pages/main/d1.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/pages/main/o0.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/pages/main/x2$a.smali` | 9 | 0 | 1 | 10 |
| `com/dragon/read/reader/ad/r.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/CdnLargeImageLoader$a.smali` | 6 | 0 | 4 | 10 |
| `com/dragon/read/util/ColorUtils.smali` | 4 | 0 | 6 | 10 |
| `com/dragon/read/util/NetworkUtils.smali` | 4 | 0 | 6 | 10 |
| `com/dragon/read/util/RecentConsumeRecorder$RecentConsumeParams.smali` | 3 | 0 | 7 | 10 |
| `com/dragon/read/util/RecentConsumeRecorder$RecentSearchParams.smali` | 3 | 0 | 7 | 10 |
| `com/dragon/read/util/UiConfigSetter$f.smali` | 3 | 0 | 7 | 10 |
| `com/dragon/read/util/k1.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/k8.smali` | 4 | 0 | 6 | 10 |
| `com/dragon/read/util/o8.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/q8.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/w8.smali` | 7 | 0 | 3 | 10 |
| `com/dragon/read/util/y$a.smali` | 6 | 0 | 4 | 10 |
| `com/ss/android/update/z$f.smali` | 7 | 0 | 3 | 10 |
| `com/ss/ttm/player/TTWindowClient.smali` | 0 | 0 | 10 | 10 |
| `an2/v.smali` | 7 | 0 | 2 | 9 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyPasswordVM.smali` | 0 | 0 | 9 | 9 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/BaseStandardHomeFragment.smali` | 0 | 0 | 9 | 9 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment.smali` | 0 | 0 | 9 | 9 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/n1.smali` | 0 | 0 | 9 | 9 |
| `com/bytedance/alliance/settings/AllianceLocalSetting$$SettingImpl.smali` | 0 | 0 | 9 | 9 |
| `com/bytedance/apm/ApmAgent.smali` | 0 | 0 | 9 | 9 |
| `com/dragon/read/ad/util/a.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/ad/util/o0.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/ad/util/q.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/ad/util/v0.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/ad/util/y.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/BindExcludeHongguoServiceImpl.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/component/biz/impl/mine/DataBinderMapperImpl.smali` | 2 | 0 | 7 | 9 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$i.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$i.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$n.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$h.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/ee.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/fb.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/gb.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/he.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/i8$b.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/component/biz/impl/mine/j9.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberOneKeyView.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/component/biz/impl/mine/na.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/pe.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/qc.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/qe.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/se.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/xh.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/MainFragmentActivity$g0.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/pages/main/e0.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/h2.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/p1.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/s1.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/reader/ad/l.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/ApkSizeOptImageLoader$a.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/FrequencyMgr$Period$Day.smali` | 5 | 0 | 4 | 9 |
| `com/dragon/read/util/ImageLoaderUtils$o.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/KeyBoardHelper.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/PictureUtils$e.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/PictureUtils$f.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/RxUtils.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/c0.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/c4.smali` | 5 | 0 | 4 | 9 |
| `com/dragon/read/util/ca.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/d6$a.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/j5.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/k$b.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/k$c.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/k6.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/k7.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/l9.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/m9.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/n5.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/s.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/y.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/y6$a.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/y7.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/y8.smali` | 6 | 0 | 3 | 9 |
| `com/ss/android/update/SSUpdateChecker.smali` | 2 | 0 | 7 | 9 |
| `com/ss/android/update/g0.smali` | 5 | 0 | 4 | 9 |
| `com/ss/android/update/k0.smali` | 5 | 0 | 4 | 9 |
| `com/ss/android/videoshop/controller/VideoController.smali` | 0 | 0 | 9 | 9 |
| `com/ss/ttm/player/MediaFormat.smali` | 0 | 0 | 9 | 9 |
| `com/ss/ttvideoengine/log/VideoEventBase.smali` | 0 | 0 | 9 | 9 |
| `com/ss/videoarch/liveplayer/model/LiveStreamInfo.smali` | 0 | 0 | 9 | 9 |
| `an2/l0.smali` | 6 | 0 | 2 | 8 |
| `an2/o0.smali` | 6 | 0 | 2 | 8 |
| `com/bytedance/apm/agent/instrumentation/SQLiteInstrumentation.smali` | 0 | 0 | 8 | 8 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/b.smali` | 3 | 0 | 5 | 8 |
| `com/dragon/read/ad/util/l.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/l0.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/n0.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/ad/util/p0.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/t.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/u.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/v.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/w.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/y0.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/z0.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/BindToutiaoServiceImpl.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$initHonorListView$1$a.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$b.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$h.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$f.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$e.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$n.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/component/biz/impl/mine/c8.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/component/biz/impl/mine/cf.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/eb.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/hc.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/k8.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/pb.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/ra.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/tc.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/ue.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/v9.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/wh.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/yf$a.smali` | 4 | 2 | 2 | 8 |
| `com/dragon/read/pages/main/MainFragmentActivity$c.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/MainFragmentActivity$x.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/MainFragmentActivity$y.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/pages/main/MiraCastMonitor$b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/pages/main/c4.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/m$a.smali` | 7 | 0 | 1 | 8 |
| `com/dragon/read/pages/main/m1.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/n.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/o1.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/p2.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/y2$a.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/z$c.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/reader/ad/b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/reader/ad/w.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/ApkSizeOptImageLoader$a$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/CdnLargeImageLoader$a$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/DragonRequestController.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/FrequencyMgr$Period$Duration7Day.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/util/ImageLoadHost$b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/ImageLoaderUtils$b.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/SetStatusBarHost.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/util/ab$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/b0.smali` | 1 | 0 | 7 | 8 |
| `com/dragon/read/util/f0$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/i5.smali` | 2 | 0 | 6 | 8 |
| `com/dragon/read/util/j6.smali` | 3 | 0 | 5 | 8 |
| `com/dragon/read/util/l8.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/la.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/n1.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/na.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/oa.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/p4.smali` | 3 | 2 | 3 | 8 |
| `com/dragon/read/util/q0.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/s9.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/u2.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/v$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/w3.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/xa.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/z2.smali` | 6 | 0 | 2 | 8 |
| `com/ss/android/update/h.smali` | 2 | 0 | 6 | 8 |
| `com/ss/android/update/t$b.smali` | 6 | 0 | 2 | 8 |
| `com/ss/android/update/z$e.smali` | 6 | 0 | 2 | 8 |
| `com/ss/ttm/player/AJMediaCodec.smali` | 0 | 0 | 8 | 8 |
| `com/ss/ttvideoengine/net/ChannelSelect.smali` | 0 | 0 | 8 | 8 |
| `com/ss/videoarch/liveplayer/model/LiveInfoSource.smali` | 0 | 0 | 8 | 8 |
| `d70/a.smali` | 0 | 0 | 8 | 8 |
| `d70/i.smali` | 0 | 0 | 8 | 8 |
| `an2/u.smali` | 5 | 0 | 2 | 7 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/UnifyPreVerifyFingerprintBaseVm.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$homePageAction$2$1.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJPayStandardResultProcess.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/u.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/VerifyPayTypeWithCombineWrapper.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyOneStepPaymentVM.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/n1$b.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/verify/utils/e.smali` | 0 | 0 | 7 | 7 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceProxy.smali` | 0 | 0 | 7 | 7 |
| `com/bytedance/apm/block/m.smali` | 0 | 0 | 7 | 7 |
| `com/dragon/read/ad/util/b1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/ad/util/h.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/ad/util/r0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/ad/util/t0.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/component/biz/impl/mine/BottomTabLandingGuideSelectionDialogLauncher$show$1$1$1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/ChangeNumServiceImpl.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$onCreate$1$2$1$1$1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$onCreateContent$controller$1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$g.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$j.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$m.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$c.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$j.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$m.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$d.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$g.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$l.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$m.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$g$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/component/biz/impl/mine/aa.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/fd.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/hg.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/hh.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/jg.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/kd$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/component/biz/impl/mine/mf.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/o9.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/od.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/rd.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/component/biz/impl/mine/rg.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/th.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/ua.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/ud.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/wd.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/FixRefreshBottomTab.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$b.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$i.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$w.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$a.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$c.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/pages/main/MiraCastMonitor$c.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/pages/main/b3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/f.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/h1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/i0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/l3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/m0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/n3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/p0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/q0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/r0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/s.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/t4$a.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/reader/ad/ReaderAdManager$d.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/reader/ad/a0$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$Companion$a.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/CoroutineExecutor.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/FrequencyMgr$Period$Never.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$b$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$j.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$n.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$q.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/PremiumReportHelper$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/util/UiConfigSetter$n$a.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/ViewStatusUtils.smali` | 2 | 0 | 5 | 7 |
| `com/dragon/read/util/b7$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/bb.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/cb.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/e2.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/f3.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/util/f7.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/f9.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/g4.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/ha.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/i7.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/ia.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/k0$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/k0.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/m4.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/m5.smali` | 2 | 0 | 5 | 7 |
| `com/dragon/read/util/o1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/o5.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/o9.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/ra.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/s0.smali` | 2 | 0 | 5 | 7 |
| `com/dragon/read/util/s1.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/t3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/t7$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/util/u3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/v3.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/w.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/x2$b.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/x5.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/y1.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/z4$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/util/z5.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/za$a.smali` | 4 | 0 | 3 | 7 |
| `com/ss/android/update/e0.smali` | 2 | 0 | 5 | 7 |
| `com/ss/android/update/j.smali` | 4 | 0 | 3 | 7 |
| `com/ss/android/update/n.smali` | 2 | 0 | 5 | 7 |
| `com/ss/android/update/q$b.smali` | 5 | 0 | 2 | 7 |
| `com/ss/android/update/s.smali` | 3 | 0 | 4 | 7 |
| `com/ss/android/update/t$a.smali` | 5 | 0 | 2 | 7 |
| `com/ss/texturerender/TextureRenderer.smali` | 0 | 0 | 7 | 7 |
| `com/ss/texturerender/effect/ICEffect/ICEffectWrapper.smali` | 0 | 0 | 7 | 7 |
| `com/ss/texturerender/effect/VideoOCLSREffect.smali` | 0 | 0 | 7 | 7 |
| `do/c$a.smali` | 0 | 0 | 7 | 7 |
| `hl/d$a.smali` | 0 | 0 | 7 | 7 |
| `an2/d.smali` | 4 | 0 | 2 | 6 |
| `an2/i.smali` | 4 | 0 | 2 | 6 |
| `an2/q0.smali` | 4 | 0 | 2 | 6 |
| `an2/w0.smali` | 3 | 0 | 3 | 6 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a0.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/payagain/applog/StdPayAgainMainLogger.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/DynamicPwdWrapper.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyFaceVM.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0$e.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/ttcjpayapi/CJPayCarrierAuthManager.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/verify/utils/h.smali` | 0 | 0 | 6 | 6 |
| `com/bytedance/alliance/services/impl/t.smali` | 0 | 0 | 6 | 6 |
| `com/bytedance/alliance/settings/AllianceOnlineSettings$$SettingImpl.smali` | 0 | 0 | 6 | 6 |
| `com/bytedance/alliance/utils/Utils.smali` | 0 | 0 | 6 | 6 |
| `com/bytedance/android/ad/reward/dynamicad/AbsRewardLynxFragment.smali` | 0 | 0 | 6 | 6 |
| `com/bytedance/android/ad/sdk/impl/advideo/monitor/AdVideoMonitorUtils.smali` | 0 | 0 | 6 | 6 |
| `com/bytedance/bdinstall/b1$a.smali` | 0 | 0 | 6 | 6 |
| `com/dragon/read/ad/util/UserRegionAdUtil.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/ad/util/a$a.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/ad/util/f1.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/ad/util/m.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/ad/util/o.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/ad/util/w0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$g.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$c.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LoginActivity$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$e.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$f.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$o.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$b.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$d.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$b.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$c.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity$a.smali` | 5 | 0 | 1 | 6 |
| `com/dragon/read/component/biz/impl/mine/ac.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ae.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/cb.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/dd.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/di.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/e.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/component/biz/impl/mine/ea.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ed.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/fh.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/gd.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/hf.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ic.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ja.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/kc.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/kf.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/lb.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/lf.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/lh.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/m.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/component/biz/impl/mine/md.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/nf.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/qa.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/qf.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/qh.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/s9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/t9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/u8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/v2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/va.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/wa.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/we.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/yd.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ye.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/z9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/MainFragmentActivity$c0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/MainFragmentActivity$e0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/a0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/a3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/b0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/b4$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/b5.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/d2.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/pages/main/g3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/m3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/o.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/o3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/q4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/r1.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/s4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/t2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/u4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/w0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/w4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/y.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/y2.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/pages/main/z2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/z3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/reader/ad/AdLine$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/reader/ad/ReaderAdManager$g.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$Companion$a$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/reader/ad/t.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/user/model/a.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/BitmapUtils$d.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/CustomTypefaceSpan.smali` | 1 | 0 | 5 | 6 |
| `com/dragon/read/util/IExtractColorHost__ServiceProxy.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/ImageLoaderUtils$c$a.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ImageLoaderUtils$k.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ImageLoaderUtils$m.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/PictureUtils$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/PictureUtils$j.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/RouterUtils.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/RxUtils$c$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/UiConfigSetter$c.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/UiConfigSetter$l.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/a9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/aa.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ba.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/c5.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/c9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/d.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/d2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/d4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/d9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/da.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/e0.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/e9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ea.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/f$d.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/fa.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/g9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ga.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/gb.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/h9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ja.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/jb.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/m.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/m3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/m7.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/n.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/n0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/n8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/n9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/o.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/o0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/o3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/o7.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/p2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/p7.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/p9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/q3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/q4.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/q9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/r7$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/r8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/r9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/s5.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/sa.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/t9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/u.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/u9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/v8.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/v9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/w9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/wa.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/x9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/y3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/y6.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/y9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/z8.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/z9.smali` | 3 | 0 | 3 | 6 |
| `com/ss/android/update/IUpdateConfig__ServiceProxy.smali` | 2 | 0 | 4 | 6 |
| `com/ss/android/update/UpdateCheckerService__ServiceProxy.smali` | 2 | 0 | 4 | 6 |
| `com/ss/android/update/UpdateService__ServiceProxy.smali` | 2 | 0 | 4 | 6 |
| `com/ss/android/update/f0.smali` | 4 | 0 | 2 | 6 |
| `com/ss/android/update/i$a.smali` | 3 | 0 | 3 | 6 |
| `com/ss/android/update/j0.smali` | 4 | 0 | 2 | 6 |
| `com/ss/android/update/l.smali` | 4 | 0 | 2 | 6 |
| `com/ss/android/update/o.smali` | 2 | 0 | 4 | 6 |
| `com/ss/android/update/q$c.smali` | 4 | 0 | 2 | 6 |
| `com/ss/android/update/u$a.smali` | 4 | 0 | 2 | 6 |
| `com/ss/android/update/y.smali` | 3 | 0 | 3 | 6 |
| `com/ss/android/update/z$h.smali` | 3 | 0 | 3 | 6 |
| `com/ss/texturerender/VideoOCLSRBmfWrapperDirectInvoke.smali` | 0 | 0 | 6 | 6 |
| `com/ss/ttvideoengine/TTTestSpeedListener.smali` | 0 | 0 | 6 | 6 |
| `com/ss/ttvideoengine/VideoCacheManager.smali` | 0 | 0 | 6 | 6 |
| `com/ss/ttvideoengine/strategy/refresh/TTVideoEngineSourceRefreshStrategy.smali` | 0 | 0 | 6 | 6 |
| `com/ss/videoarch/liveplayer/effect/VeLivePlayerVideoEffectManager.smali` | 0 | 0 | 6 | 6 |
| `p8/f.smali` | 0 | 0 | 6 | 6 |
| `tj/a.smali` | 0 | 0 | 6 | 6 |
| `xc/e.smali` | 0 | 0 | 6 | 6 |
| `xf/f.smali` | 0 | 0 | 6 | 6 |
| `an2/f0.smali` | 3 | 0 | 2 | 5 |
| `an2/h.smali` | 3 | 0 | 2 | 5 |
| `an2/h0.smali` | 3 | 0 | 2 | 5 |
| `an2/j0.smali` | 2 | 0 | 3 | 5 |
| `an2/s.smali` | 2 | 0 | 3 | 5 |
| `an2/s0.smali` | 3 | 0 | 2 | 5 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/j.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainGuideFragment.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMethodFragment.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/e.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/alliance/services/impl/d.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/alliance/services/impl/h.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/android/ad/preload/session/i.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/apm/agent/instrumentation/okhttp3/OkHttpRecord.smali` | 0 | 0 | 5 | 5 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$WXJumpInfoResponse$DataModel.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$WXJumpInfoResponse.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/c.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/c1$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/ad/util/g0.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/s.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/ad/util/x.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$d.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$g.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$h$b.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$i.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenLoginActivity$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$b$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/component/biz/impl/mine/HongguoPreferenceServiceImpl.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/HongguoRedDotListenListCreator.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$b$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$d.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$k.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$l.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$p.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$j.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ab.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/bb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/cc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/dc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/de.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ef.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/fi.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ie.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/jb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/je.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/kb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ke.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/kg.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/lc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/le.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/h.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/component/biz/impl/mine/m3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/mb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/md$a.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/component/biz/impl/mine/me.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/mh.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/nh.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/qd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/rb.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/s3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ta.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/tb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/uc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/vc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/xa.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/yc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/za.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ze.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/MainFragmentActivity$d.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/MainFragmentActivity$n.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$SavedState.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$d.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/pages/main/c0.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/pages/main/d.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/d3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/d4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/g4$a.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/pages/main/h3$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/pages/main/k3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/l0.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/l4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/r.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/t.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/t0.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/u.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/u0.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/u1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/v1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/w1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/x.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/z$d.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/OfflineDefaultAdLine$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/ReaderAdManager$b.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/ReaderAdManager$e.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/ReaderAdManager$j.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/ReaderAdManager$k.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/m.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/n.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/o.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/q.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/reader/ad/z.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/user/model/PrivilegeInfoModel$InspiresBookPrivilege.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/user/model/PrivilegeInfoModel$OfflineReadBook.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/user/model/VipInfoModel.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/AnimationViewWrapper.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/ContextKt.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/FixedSizeArrayDeque.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/util/ImageLoaderUtils$c.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/ImageLoaderUtils$h.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/ImageLoaderUtils$t.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/ImageLoaderUtils$v.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/KeyBoardHelper$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/KeyBoardHelper$b.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/PictureUtils$c.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/RxUtils$b$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/UiConfigSetter$e$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/UiConfigSetter$n$b.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/b2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/b9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/e3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/eb.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/f$b.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/f$f.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/f6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/fb.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/util/g.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/g6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/h4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/h6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/hb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/i9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/j2.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/j5$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/util/j9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/k9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/ka.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/kb.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/l5$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/util/m$a.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/m$b.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/n7.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/na$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/q1.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/r4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/r5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/s4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/t1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/t2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/t6.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/t7.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/u5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/u7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/ua.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/x2$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/x8.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/y2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/y5.smali` | 3 | 0 | 2 | 5 |
| `com/ss/android/update/UpdateCheckerService$1.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/UpdateProgressActivity$f.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/d0.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/s$a.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/u$d.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/z$g.smali` | 1 | 0 | 4 | 5 |
| `com/ss/texturerender/effect/AdaptiveSharpenEffect.smali` | 0 | 0 | 5 | 5 |
| `com/ss/ttm/player/TTPlayerView.smali` | 0 | 0 | 5 | 5 |
| `com/ss/ttvideoengine/strategrycenter/StrategyEvent.smali` | 0 | 0 | 5 | 5 |
| `com/ss/videoarch/liveplayer/PreloadHelper$PreloadEventHandler.smali` | 0 | 0 | 5 | 5 |
| `d70/c.smali` | 0 | 0 | 5 | 5 |
| `d70/k.smali` | 0 | 0 | 5 | 5 |
| `ui/d.smali` | 0 | 0 | 5 | 5 |
| `w20/i.smali` | 0 | 0 | 5 | 5 |
| `wj/b.smali` | 0 | 0 | 5 | 5 |
| `zd/b.smali` | 0 | 0 | 5 | 5 |
| `zd/c.smali` | 0 | 0 | 5 | 5 |
| `an2/a.smali` | 2 | 0 | 2 | 4 |
| `an2/e.smali` | 2 | 0 | 2 | 4 |
| `an2/m.smali` | 2 | 0 | 2 | 4 |
| `an2/m0.smali` | 2 | 0 | 2 | 4 |
| `an2/n0.smali` | 2 | 0 | 2 | 4 |
| `an2/o.smali` | 2 | 0 | 2 | 4 |
| `an2/p0.smali` | 2 | 0 | 2 | 4 |
| `an2/r0.smali` | 2 | 0 | 2 | 4 |
| `an2/t0.smali` | 2 | 0 | 2 | 4 |
| `an2/v0.smali` | 2 | 0 | 2 | 4 |
| `an2/x.smali` | 2 | 0 | 2 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/i.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/y.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/q$d.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/b.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/FrontMethodFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/FrontRetryCombinePayFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/e.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/l.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/g.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/activity/CJPaySSAgreementActivity.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSSmsVerifyFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/utils/CreditPayProcessUtils.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/i.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l1.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/o0.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p0.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p1.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/b.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/verify/activity/DyStepUpIFrameActivity.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/verify/jsb/c.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsFragment.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/services/impl/InstrumentationServiceImpl.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/services/impl/a.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/services/impl/r0.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/settings/AllianceMultiProcessLocalSetting$$SettingImpl.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/apm/agent/instrumentation/transaction/TxState.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/apm/config/h.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/apm/internal/ApmDelegate.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/applog/priority/original/CommonKt.smali` | 0 | 0 | 4 | 4 |
| `com/dragon/read/ad/util/m0.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/ad/util/p.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$e.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$h$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/DiggContentActivity$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenBindDouyinActivity$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$k.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$n.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$h.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$f.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$g$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$g$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$l.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$n.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/a.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/ad.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/b9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ba.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/be.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/bg.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/cd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/cg.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ci.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/d8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/da.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/db.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ec.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/f8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/fa.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/fe.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/g.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/g9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/gc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/gf.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/gg.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/gh.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/hb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/i9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/id.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/ih.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/jc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/jd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/jf.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ka.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/l8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ld.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/g.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/ma.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/mc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/n.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/n9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/nd.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/ne.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ob.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/oc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/p.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/p9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/pa.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/pd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/pf.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/r9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/rc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/s.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/s8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/sc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/t.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/t8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/td.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/te.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/tf.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/vd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ve.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/wc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/x8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/xc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/xd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/xe.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/z8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/zc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/zd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$f0.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$k.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$p.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$t.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$u.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$v.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$z.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$b.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/pages/main/a2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/a4$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/a5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/b4$b$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/c1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/c3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/c5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/e1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/e2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/f0.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/f1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/f3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/f4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/g1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/h4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/i1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/i4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/j1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/j2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/j4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/l1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/q2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/q3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/r2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/r3$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/s2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/s3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/t1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/t3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/u2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/u3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/v0.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/v3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/v4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/x4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/y2$a$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/y4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/z1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/z2$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/reader/ad/ReaderAdManager$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/reader/ad/ReaderAdManager$i.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/reader/ad/u.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/BookUtils$a.smali` | 3 | 0 | 1 | 4 |
| `com/dragon/read/util/DebugManager$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ImageLoaderUtils$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ImageLoaderUtils$e.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ImageLoaderUtils$f.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ImageLoaderUtils$g.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ImageLoaderUtils$i.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ImageLoaderUtils$l.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/PictureUtils$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/PictureUtils$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/RxUtils$b.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/RxUtils$c.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$c.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$d.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$e.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$f.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$g.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$h.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$i.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$j.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ToastUtils$k.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/UiConfigSetter$a.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/UiConfigSetter$g.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/UiUtils$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/a3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/a4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/a5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/a6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/b1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/b3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/c6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/c8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/d1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/d7$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/da$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/e8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/f$e.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/g7$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/g7$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/g7$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/h2$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/h2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/h3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/h7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/i1.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/i6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/j0.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/j4$a.smali` | 3 | 0 | 1 | 4 |
| `com/dragon/read/util/l3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/l7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ma.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/n3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/o2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/oa$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/p3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/p5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/q.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/q2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/q6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/r3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/r6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/s2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/s8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/s9$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/t5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/t8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/u8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/v2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/v4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/w2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/w5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/x6.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/ya$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ya.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/z3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/za.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/MaxSizeLinearLayout.smali` | 1 | 0 | 3 | 4 |
| `com/ss/android/update/UpdateProgressActivity$a.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/UpdateProgressActivity$b.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/UpdateProgressActivity$c.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/UpdateProgressActivity$d.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/UpdateProgressActivity$e.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/a0.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/c0.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/h0.smali` | 1 | 0 | 3 | 4 |
| `com/ss/android/update/k.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/p.smali` | 1 | 0 | 3 | 4 |
| `com/ss/android/update/q$a.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/u$b.smali` | 2 | 0 | 2 | 4 |
| `com/ss/android/update/u$c.smali` | 1 | 0 | 3 | 4 |
| `com/ss/android/update/z$d.smali` | 2 | 0 | 2 | 4 |
| `com/ss/texturerender/VideoOCLSRBmfWrapper.smali` | 0 | 0 | 4 | 4 |
| `com/ss/texturerender/effect/GLGaussianBlurFilter.smali` | 0 | 0 | 4 | 4 |
| `com/ss/texturerender/effect/GLOesTo2DFilter.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/SubDesInfoModel.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/TTNetWorkListener.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$6.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/configcenter/ConfigItemFactory.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/playermetrcis/PlayerMetrics.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/source/strategy/CodecStrategy.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/strategrycenter/StrategyHelper$MyAppServer.smali` | 0 | 0 | 4 | 4 |
| `com/ss/ttvideoengine/strategy/StrategyManager.smali` | 0 | 0 | 4 | 4 |
| `com/ss/videoarch/live/ttquic/PreloadManager.smali` | 0 | 0 | 4 | 4 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$TTLiveSurfaceCallback.smali` | 0 | 0 | 4 | 4 |
| `d70/g.smali` | 0 | 0 | 4 | 4 |
| `e30/g.smali` | 0 | 0 | 4 | 4 |
| `kn/i.smali` | 0 | 0 | 4 | 4 |
| `l40/d.smali` | 0 | 0 | 4 | 4 |
| `oe/h$a.smali` | 0 | 0 | 4 | 4 |
| `t30/k.smali` | 0 | 0 | 4 | 4 |
| `uc/a.smali` | 0 | 0 | 4 | 4 |
| `wi/f.smali` | 0 | 0 | 4 | 4 |
| `zd/a.smali` | 0 | 0 | 4 | 4 |
| `zd/d.smali` | 0 | 0 | 4 | 4 |
| `an2/a1.smali` | 1 | 0 | 2 | 3 |
| `an2/d0.smali` | 1 | 0 | 2 | 3 |
| `an2/l.smali` | 1 | 0 | 2 | 3 |
| `an2/y0.smali` | 1 | 0 | 2 | 3 |
| `b98/c.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/e$d.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/e.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/m$b.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/o.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/s.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/t.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/x.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPrePayProcess.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/e.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/q.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardHomeManager.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardPayTypeWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayCommonUtils$a.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMainFragment$d.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMainFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/p.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/q.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/activity/CJPaySSSmsVerifyActivity.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/activity/CJPaySSUpdateCardInfoActivity.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyFingerPrintPreHalfWindowFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/PwdBaseWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/y.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/c.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/k.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/m1.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/o1.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/r0.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/verify/utils/DyVerifyCertOperate.smali` | 0 | 0 | 3 | 3 |
| `com/awesome/fqhybrid/core/FqAnnieXCardLynxEngineProxy.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/ad/gip/WindMillDetailFragment.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/alliance/core/AllianceServiceImpl.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/android/ad/sdk/impl/ipc/AdIpcDepend.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/apm/ApmContext.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/apm/util/CommonMonitorUtil.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/apm/util/MultiProcessSharedPreferences.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/article/common/utils/ConcaveScreenUtils.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/bdinstall/d.smali` | 0 | 0 | 3 | 3 |
| `com/dragon/read/ad/util/b0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/d0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/d1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/e0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/e1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/f0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/k.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/m0$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/base/ssconfig/model/MotionComicPatchAdConfig.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$h$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/DataBinderMapperImpl$a.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/component/biz/impl/mine/DataBinderMapperImpl$b.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/component/biz/impl/mine/ExcludeFanqieServiceImpl.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenBindDouyinActivity$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenLoginActivity$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$g.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$i.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/NewBindHongguoServiceImpl.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$d.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/a0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/a1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/a2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/af.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ah.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/b0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/b1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/b2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ca.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard$updateTrebleFuncLayout$gridLayoutManager$1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/d0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/d1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/d2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/eg.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/f0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/f1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/f2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/f9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ff.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/g0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/g1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/g2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/g8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ge.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/i0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/i1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/i2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ib.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/j0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/j1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/j2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/jh.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/kh.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/l0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/l1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/l2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/l9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/d.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/m0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/m1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/m2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/mg.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/nb.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ng.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/o0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/o1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/o2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/oe.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/og.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/oh.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/p0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/p1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/p2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/q0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/q1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/q2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/r0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/r1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/r2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/rh.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s6.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/component/biz/impl/mine/sb.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/t0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/t1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/t2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/td$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/uf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ug.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/uh.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/vf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/w0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/w1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/wf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/x0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/x1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/x9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/xf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ya.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/zb.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/FixRefreshBottomTab$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$g.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$l.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$m.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$o.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/a1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/a4$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/b1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/b2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/b4$b$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/e0$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/e0$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/e4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/g2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/k0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/l2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/n1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/n4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/o4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/p3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/x2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/y0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/y3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/z0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/ReaderAdManager$h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/g.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/h$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/i$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/p.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/y.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/AnimationViewWrapper$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BitmapUtils$LocalImageData.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BitmapUtils$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BitmapUtils$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BitmapUtils$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BitmapUtils$d$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BitmapUtils$e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/BookNameType$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/CommonUiFlow$CommonUiFlowException.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/CommonUiFlow$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/CommonUiFlow$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/DebugManager$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ExtractColorHost$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/FileUtils$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/FrequencyMgr$Period.smali` | 0 | 0 | 3 | 3 |
| `com/dragon/read/util/FrequencyMgr$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ImageLoadHost$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ImageLoaderUtils$p.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ImageLoaderUtils$s.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/OOMScoreAdjUtil$OOMAdjType$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/PictureUtils$h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/PictureUtils$i.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/RxUtils$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/SetStatusBarHost$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ToastUtils$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ToastUtils$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/UiConfigSetter$j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/UiUtils$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/UiUtils$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/UiUtils$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ViewStatusUtils$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ViewStatusUtils$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ViewStatusUtils$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ViewStatusUtils$d.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/a8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/c7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/d$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/d3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/d8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/e4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/e7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/f$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/f0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/g7$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/g7$e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/g7$f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/g8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/h1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/h8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/i8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/j2$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/j8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/k$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/l6.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/m2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/m6.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/m8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/o4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/p.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/p8$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/pa.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/r1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/s3$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/s3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/v0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/v6.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/util/va.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/w0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/x.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/x7$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z4.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/b0.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/i0.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/m.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/o$a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/q$d.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/t$c.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/w$a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/w.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/x$a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/z$c.smali` | 1 | 0 | 2 | 3 |
| `com/ss/bduploader/smartserver/SmartRouting.smali` | 0 | 0 | 3 | 3 |
| `com/ss/mediakit/net/AVMDLDNSInfo.smali` | 0 | 0 | 3 | 3 |
| `com/ss/mediakit/net/AVMDLMultiNetwork.smali` | 0 | 0 | 3 | 3 |
| `com/ss/mediakit/net/HTTPDNSHosts.smali` | 0 | 0 | 3 | 3 |
| `com/ss/texturerender/TextureRenderManager.smali` | 0 | 0 | 3 | 3 |
| `com/ss/texturerender/VideoSurface.smali` | 0 | 0 | 3 | 3 |
| `com/ss/texturerender/effect/GLBrightnessBalanceFilter.smali` | 0 | 0 | 3 | 3 |
| `com/ss/texturerender/effect/vr/GLPanorama180To360Filter.smali` | 0 | 0 | 3 | 3 |
| `com/ss/texturerender/effect/vr/GLPanoramaFilter.smali` | 0 | 0 | 3 | 3 |
| `com/ss/texturerender/overlay/OverlayVideoTextureRenderer.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttm/player/TTPlayerViewHelper.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttm/player/TTSurfaceView$1.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/AppInfo.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/PreloaderURLItem.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/PreloaderVidItem.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/PreloaderVideoModelItem.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/SubModel.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$MyLoggerDataSource.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/TTVideoEngineInternal.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/TTVideoEngineSurfaceCallback.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/log/HeadsetStateHistory.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/log/VideoEventOneEvent.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/log/VideoEventOneNoRender.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/selector/strategy/GearStrategy.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/strategrycenter/StrategyHelper.smali` | 0 | 0 | 3 | 3 |
| `com/ss/ttvideoengine/utils/MDLExtraInfoHelper.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/live/LiveIOWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/liveplayer/VLDNSParserImpl.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/liveplayer/retry/RetryProcessor.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/liveplayer2/VeLivePlayer$1.smali` | 0 | 0 | 3 | 3 |
| `d30/b.smali` | 0 | 0 | 3 | 3 |
| `d70/b.smali` | 0 | 0 | 3 | 3 |
| `d8/a$a.smali` | 0 | 0 | 3 | 3 |
| `e30/e.smali` | 0 | 0 | 3 | 3 |
| `e30/f.smali` | 0 | 0 | 3 | 3 |
| `e8/c.smali` | 0 | 0 | 3 | 3 |
| `e80/m.smali` | 0 | 0 | 3 | 3 |
| `eb/g.smali` | 0 | 0 | 3 | 3 |
| `fb/e.smali` | 0 | 0 | 3 | 3 |
| `g60/d.smali` | 0 | 0 | 3 | 3 |
| `g60/j.smali` | 0 | 0 | 3 | 3 |
| `il/b.smali` | 0 | 0 | 3 | 3 |
| `kp/a.smali` | 0 | 0 | 3 | 3 |
| `la/a.smali` | 0 | 0 | 3 | 3 |
| `lf/a.smali` | 0 | 0 | 3 | 3 |
| `nd/j.smali` | 0 | 0 | 3 | 3 |
| `oe/g.smali` | 0 | 0 | 3 | 3 |
| `oe/h.smali` | 0 | 0 | 3 | 3 |
| `q20/a.smali` | 0 | 0 | 3 | 3 |
| `q30/g.smali` | 0 | 0 | 3 | 3 |
| `q60/d.smali` | 0 | 0 | 3 | 3 |
| `qe/c.smali` | 0 | 0 | 3 | 3 |
| `qi/d.smali` | 0 | 0 | 3 | 3 |
| `sq/g.smali` | 0 | 0 | 3 | 3 |
| `t20/a.smali` | 0 | 0 | 3 | 3 |
| `t40/b.smali` | 0 | 0 | 3 | 3 |
| `ui/l.smali` | 0 | 0 | 3 | 3 |
| `w20/g.smali` | 0 | 0 | 3 | 3 |
| `w60/e.smali` | 0 | 0 | 3 | 3 |
| `wd/a.smali` | 0 | 0 | 3 | 3 |
| `wd/b.smali` | 0 | 0 | 3 | 3 |
| `x60/c$a.smali` | 0 | 0 | 3 | 3 |
| `x60/d.smali` | 0 | 0 | 3 | 3 |
| `xc/c.smali` | 0 | 0 | 3 | 3 |
| `xq/a.smali` | 0 | 0 | 3 | 3 |
| `zi/c.smali` | 0 | 0 | 3 | 3 |
| `a98/c.smali` | 0 | 0 | 2 | 2 |
| `an2/j0$a.smali` | 1 | 0 | 1 | 2 |
| `an2/k.smali` | 1 | 0 | 1 | 2 |
| `b88/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a$d.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/d0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/e.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/t$b.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/v.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/m.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/n.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/j$c.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/l.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/f.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/g.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/d.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/f.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/g.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/CJUnifyPayCommonHttpParamsUtil.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/FrontCounterProvider.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/g.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/q.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/b$a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideVoucherHalfWrapper.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSAgreementDetailFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSAgreementListFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSSmsReceivedExceptionFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSUpdateCardInfoFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/c.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyAgreementDetailFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyOneStepPayFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFullFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/r0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyOneStepPaymentVM$e.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/h.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/m0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/s0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/w0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0$i.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/AudioHelper.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/SAMICoreDeNoise.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/n.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/VoicePrintActivity.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/VoicePrintController$a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/VoicePrintFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$handleCreateOrderAndPay$1.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/jsb/VerifyBizJsbImpl.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/utils/DyVerifyCertOperate$a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/utils/DyVerifyCertOperate$d.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifyCertFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifyPasswordFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$c.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/vm/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/vm/d.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/verify/vm/e.smali` | 0 | 0 | 2 | 2 |
| `com/awesome/fqhybrid/bridge/impl/f.smali` | 0 | 0 | 2 | 2 |
| `com/awesome/fqhybrid/service/FqLynxBizService$b.smali` | 0 | 0 | 2 | 2 |
| `com/awesome/fqhybrid/service/FqLynxBizService.smali` | 0 | 0 | 2 | 2 |
| `com/byted/mgl/merge/service/api/share/BdpShareBaseInfo.smali` | 0 | 0 | 2 | 2 |
| `com/byted/mgl/merge/service/api/share/ShareImCallbackInfo.smali` | 0 | 0 | 2 | 2 |
| `com/byted/mgl/merge/service/model/BdpLocation.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/accountseal/view/BdAccountSealActivity.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/ad/live/component/sif/WindmillServiceWithSif.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/ad/live/component/sif/lynxbridge/d0.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$2.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$config$1$getNextInspireCallback$1.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$config$1$launchRequestNextRewardInfo$1.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/AdEventImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/InspireAdInitConfigImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/InspireAdRequestImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/NetworkImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/base/component/BaseRemoteViewsService.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/bean/PassData.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/services/impl/a0$a.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/services/impl/a0.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/services/impl/b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/services/impl/e.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/utils/b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/utils/e.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/bridges/bridge/base/g.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/bridges/log/SifLog$a.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/preload/util/AdPreloadTrace.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/reward/dynamicad/AbsRewardLynxFragment$b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/rewarded/draw/DrawAdLoadMoreDispatcher.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/rewarded/draw/RewardAdDrawFragment$b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/sdk/api/ipc/AbsAdIpcAsyncMethod.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/sdk/impl/settings/SettingsManager.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/sdk/pitaya/AdIpcPitayaLLMRunTaskMethod.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceCapabilityFactory.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/anniex/bd/foundation/impl/s.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/instrumentation/ClickInstrumentation.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/instrumentation/okhttp3/OkHttpEventListener.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/tracing/AutoLaunchTraceHelper.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/v2/instrumentation/ClickAgent.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/config/ApmStartConfig$Builder.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/report/FileUploadServiceImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/util/TrafficUtils.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm6/consumer/slardar/send/b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/applog/et_verify/EventVerify.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/applog/priority/original/Engine.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/applog/priority/original/w.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdinstall/a1.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdinstall/c1.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdinstall/j0.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdinstall/p0.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdinstall/t0.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/bdinstall/u0.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/base/AbsActivity.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$initFunctionListWithSideBar$1.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$i.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$k.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/i8$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/LoginTypeView$ShowType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/a$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/b$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/e$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/i$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/j$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/k$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/nc$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/sd.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/sf.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/IFixRefreshBottomTab$$Impl$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/MainFragmentActivity$e.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$SavedState$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/MiraCastMonitor$JudgmentType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/pages/main/MiraCastMonitor$MiraCastState.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/pages/main/c2.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/g$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/n2.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/o2.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/s0.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/w3.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/z$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/user/model/NetIdLoginResp$Status.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/CdnImageCacheEventListener$Scene.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/CustomFrescoMonitor$DownSampleType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/DragonRequestController$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/LoadImageCallback$DefaultImpls.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/OOMScoreAdjUtil$OOMAdjType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/PremiumReportHelper$PayEntryType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/RealBookType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/RecentConsumeType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/RequestScene.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/UiConfigSetter$ConstraintType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/UiConfigSetter$SetTimingType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/UiConfigSetter$l$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/c.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/c2$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/e.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/f7$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/g3.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/k0$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/l.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/l4.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/l5.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/l7$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/p6.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/q7.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/u0.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/u1.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/v1.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/v7.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/w1$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/w4.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/w6.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/x7$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/y4.smali` | 1 | 0 | 1 | 2 |
| `com/ss/android/update/g.smali` | 1 | 0 | 1 | 2 |
| `com/ss/android/update/i$b.smali` | 1 | 0 | 1 | 2 |
| `com/ss/android/update/j0$a.smali` | 1 | 0 | 1 | 2 |
| `com/ss/android/videoshop/context/VideoContext.smali` | 0 | 0 | 2 | 2 |
| `com/ss/android/videoshop/mediaview/LayerHostMediaLayout.smali` | 0 | 0 | 2 | 2 |
| `com/ss/android/videoshop/mediaview/f.smali` | 0 | 0 | 2 | 2 |
| `com/ss/android/videoshop/mediaview/p.smali` | 0 | 0 | 2 | 2 |
| `com/ss/bduploader/net/HTTPDNS.smali` | 0 | 0 | 2 | 2 |
| `com/ss/bduploader/smartserver/SmartSpeedTest.smali` | 0 | 0 | 2 | 2 |
| `com/ss/mediakit/downloader/AVMDLDownLoadTask.smali` | 0 | 0 | 2 | 2 |
| `com/ss/mediakit/fetcher/AVMDLURLFetcherBridge.smali` | 0 | 0 | 2 | 2 |
| `com/ss/mediakit/net/HTTPDNS.smali` | 0 | 0 | 2 | 2 |
| `com/ss/mediakit/net/IPCache.smali` | 0 | 0 | 2 | 2 |
| `com/ss/texturerender/FrameRenderChecker.smali` | 0 | 0 | 2 | 2 |
| `com/ss/texturerender/effect/BMFFrameEvaluation.smali` | 0 | 0 | 2 | 2 |
| `com/ss/texturerender/effect/GLAnimationFilter.smali` | 0 | 0 | 2 | 2 |
| `com/ss/texturerender/effect/GLSelectiveGaussianBlurFilterOpt.smali` | 0 | 0 | 2 | 2 |
| `com/ss/texturerender/effect/vr/director/sensordirector/SensorDirector.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttm/player/AJMediaCodec$1.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttm/player/TTCrashUtil.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttm/player/TTPlayerClient.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttm/player/TTSurfaceView.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttm/player/VsyncTimeHelper$UIVSyncSampler.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/EngineAdapter.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/MediaTrackInfoModel.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$MySubFetcherListener.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/configcenter/PlayerConfigExecutor.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/database/VideoModelDBManager.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/download/DownloadTask.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/download/DownloadVidTask.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/download/Downloader.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/drm/DrmUtils.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/fetcher/SubInfoFetcher.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/fetcher/VideoInfoFetcher.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/httpdns/BytedanceHTTPDNSParser.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/log/DeviceMonitorUtils.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/log/VideoEventBase$MDLTrackInfo.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/log/VideoEventOneOpera.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/log/VideoEventOneOutSync.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/log/VideoEventOnePlay.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/model/IntertrustDrmHelper.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/model/VideoInfo.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/net/DNSParser.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/net/HTTPDNS.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/net/TTHTTPNetwork$3.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/preRender/PlayBuffer.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/preRender/PlayBufferManager.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/setting/SettingsHelper.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/source/VidPlayAuthTokenSource$Builder.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/source/strategy/CodecStrategy$Decoder.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/source/strategy/CodecStrategyAdapter$PlayerSourceSetter.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/source/strategy/CodecStrategyAdapter$PreloadSourceSetter$-CC.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/utils/DisplayMode.smali` | 0 | 0 | 2 | 2 |
| `com/ss/ttvideoengine/utils/PlayDurationManager.smali` | 0 | 0 | 2 | 2 |
| `com/ss/vcbkit/a.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/log/LiveApplog.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/log/LiveError.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/medialoader/MediaLoaderWrapper.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/utils/LiveUtils.smali` | 0 | 0 | 2 | 2 |
| `d70/d.smali` | 0 | 0 | 2 | 2 |
| `d70/e.smali` | 0 | 0 | 2 | 2 |
| `d70/j.smali` | 0 | 0 | 2 | 2 |
| `dj/c.smali` | 0 | 0 | 2 | 2 |
| `dl/i0.smali` | 0 | 0 | 2 | 2 |
| `dl/j0.smali` | 0 | 0 | 2 | 2 |
| `dn/b.smali` | 0 | 0 | 2 | 2 |
| `do/c.smali` | 0 | 0 | 2 | 2 |
| `do/f.smali` | 0 | 0 | 2 | 2 |
| `e40/a.smali` | 0 | 0 | 2 | 2 |
| `e50/b.smali` | 0 | 0 | 2 | 2 |
| `e80/g.smali` | 0 | 0 | 2 | 2 |
| `e80/z.smali` | 0 | 0 | 2 | 2 |
| `eb/f.smali` | 0 | 0 | 2 | 2 |
| `eh/f.smali` | 0 | 0 | 2 | 2 |
| `eh/h.smali` | 0 | 0 | 2 | 2 |
| `eh/k.smali` | 0 | 0 | 2 | 2 |
| `el/e.smali` | 0 | 0 | 2 | 2 |
| `en/f.smali` | 0 | 0 | 2 | 2 |
| `eo/b.smali` | 0 | 0 | 2 | 2 |
| `f50/d.smali` | 0 | 0 | 2 | 2 |
| `f9/c$b.smali` | 0 | 0 | 2 | 2 |
| `f9/c$f.smali` | 0 | 0 | 2 | 2 |
| `f9/f.smali` | 0 | 0 | 2 | 2 |
| `f9/g.smali` | 0 | 0 | 2 | 2 |
| `f9/n.smali` | 0 | 0 | 2 | 2 |
| `f9/o.smali` | 0 | 0 | 2 | 2 |
| `fb/b.smali` | 0 | 0 | 2 | 2 |
| `fb/g.smali` | 0 | 0 | 2 | 2 |
| `g40/d.smali` | 0 | 0 | 2 | 2 |
| `g60/h.smali` | 0 | 0 | 2 | 2 |
| `gh/a$a.smali` | 0 | 0 | 2 | 2 |
| `gh/a.smali` | 0 | 0 | 2 | 2 |
| `h40/g.smali` | 0 | 0 | 2 | 2 |
| `h70/f.smali` | 0 | 0 | 2 | 2 |
| `h9/d$a.smali` | 0 | 0 | 2 | 2 |
| `hb/c.smali` | 0 | 0 | 2 | 2 |
| `hl/d.smali` | 0 | 0 | 2 | 2 |
| `hp/a$a.smali` | 0 | 0 | 2 | 2 |
| `ih/a.smali` | 0 | 0 | 2 | 2 |
| `ii/b.smali` | 0 | 0 | 2 | 2 |
| `ii/d.smali` | 0 | 0 | 2 | 2 |
| `j40/b.smali` | 0 | 0 | 2 | 2 |
| `jb/h.smali` | 0 | 0 | 2 | 2 |
| `k8/a.smali` | 0 | 0 | 2 | 2 |
| `kk/a.smali` | 0 | 0 | 2 | 2 |
| `l40/e$c.smali` | 0 | 0 | 2 | 2 |
| `la/e.smali` | 0 | 0 | 2 | 2 |
| `lc/l.smali` | 0 | 0 | 2 | 2 |
| `lp/b.smali` | 0 | 0 | 2 | 2 |
| `ma/c.smali` | 0 | 0 | 2 | 2 |
| `mb/m.smali` | 0 | 0 | 2 | 2 |
| `mf/a.smali` | 0 | 0 | 2 | 2 |
| `nl/a.smali` | 0 | 0 | 2 | 2 |
| `oc/a.smali` | 0 | 0 | 2 | 2 |
| `oi/c.smali` | 0 | 0 | 2 | 2 |
| `oi/d.smali` | 0 | 0 | 2 | 2 |
| `pa/a.smali` | 0 | 0 | 2 | 2 |
| `pm/b.smali` | 0 | 0 | 2 | 2 |
| `q30/c.smali` | 0 | 0 | 2 | 2 |
| `qf/f.smali` | 0 | 0 | 2 | 2 |
| `qg/f.smali` | 0 | 0 | 2 | 2 |
| `qi/c.smali` | 0 | 0 | 2 | 2 |
| `qi/d$a.smali` | 0 | 0 | 2 | 2 |
| `qi/d$b.smali` | 0 | 0 | 2 | 2 |
| `qi/d$e.smali` | 0 | 0 | 2 | 2 |
| `qi/f.smali` | 0 | 0 | 2 | 2 |
| `rk/a.smali` | 0 | 0 | 2 | 2 |
| `s60/c.smali` | 0 | 0 | 2 | 2 |
| `sa/a.smali` | 0 | 0 | 2 | 2 |
| `sc/a.smali` | 0 | 0 | 2 | 2 |
| `sj/d.smali` | 0 | 0 | 2 | 2 |
| `t30/d$a.smali` | 0 | 0 | 2 | 2 |
| `t40/c.smali` | 0 | 0 | 2 | 2 |
| `tb/a.smali` | 0 | 0 | 2 | 2 |
| `tj/f.smali` | 0 | 0 | 2 | 2 |
| `tq/a.smali` | 0 | 0 | 2 | 2 |
| `uc/a$a.smali` | 0 | 0 | 2 | 2 |
| `um/c.smali` | 0 | 0 | 2 | 2 |
| `w20/k.smali` | 0 | 0 | 2 | 2 |
| `w30/g.smali` | 0 | 0 | 2 | 2 |
| `w70/a.smali` | 0 | 0 | 2 | 2 |
| `w8/a.smali` | 0 | 0 | 2 | 2 |
| `x60/e.smali` | 0 | 0 | 2 | 2 |
| `xa/a.smali` | 0 | 0 | 2 | 2 |
| `xf/e.smali` | 0 | 0 | 2 | 2 |
| `xf/i.smali` | 0 | 0 | 2 | 2 |
| `zd/e$a.smali` | 0 | 0 | 2 | 2 |
| `zd/f.smali` | 0 | 0 | 2 | 2 |
| `zi/b.smali` | 0 | 0 | 2 | 2 |
| `a68/b.smali` | 0 | 0 | 1 | 1 |
| `an2/b1.smali` | 1 | 0 | 0 | 1 |
| `ca8/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$startVerify$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyPasswordVM$PageType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyPasswordVM$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyVoiceVM$showMicrophonePermissionSettingsDialog$settingsDialog$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/e$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/j$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/UnifyPreVerifyPwdWrapper$getLynxKeepDialogEventHandler$5.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/UnifyPreVerifyPwdWrapper$initForgetPwdView$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/UnifyPreVerifyPwdWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess$BindCardStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess$handlePreChargeResp$dialog$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess$start$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayCreditPayProcess$start$1$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayCreditPayProcess$start$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayCreditPayProcess.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayDirectBankProcess$ResultStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayIncomePayProcess$goToLynxOpenAccount$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPrePayProcess$bindCardCallback$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPrePayProcess$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/contract/CJUnifyPayProcessState.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/contract/CJUnifyPreProcessCode.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/q$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/r.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/s.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/t.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/result/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$bindLargeScreenHostIfNeeded$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$handleStdJumpPrePayResult$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$homePageAction$2$1$onCombineCardChangeClick$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$onCreate$46.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$preVerifyListener$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$refreshMethodList$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$tryCloseWithKeepDialog$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$tryCloseWithKeepDialog$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$tryCloseWithKeepDialog$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJPayStandardResultProcess$k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJStandardPayProcess$doubleCheckProcess$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJStandardTradeQueryRespWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/w.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/x.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$bindBottomArea$2$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$buildKeepDialogConfig$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$6.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$7$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$7.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$renderFaceRecommendGuide$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$wrapBankCardPointSwitchListenerForReport$1$onSwitchChange$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$wrapBankCardPointSwitchListenerForReport$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmPopHandler$interceptIfNeeded$dialog$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmPopHandler$interceptIfNeeded$dialog$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/BaseStandardHomeFragment$renderPreSignGuide$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/BaseStandardHomeFragment$setNoPwdGuideView$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardCvvContentController$onBind$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardCvvFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardHomePageWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardPasswordFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardSmsContentController$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardSmsContentController$onBind$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardSmsContentController$schedulePanelOverflowCheck$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardSmsFragment$createContentController$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardSmsFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/marketing/CJStandardDiscountWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/marketing/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/marketing/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodWrapper$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardButtonInfoDialogHandler.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardKeepDialogController$buildKeepDialogEventHandlers$12.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardKeepDialogController$buildKeepDialogEventHandlers$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardKeepDialogController$buildKeepDialogEventHandlers$9.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$13.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$16.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$17.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$8.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$9.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$showRetainDialog$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/k$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/m$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyLayoutInflaterPreload.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$reportBTM$eventHandlers$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$reportBTM$eventHandlers$20.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$reportBTM$eventHandlers$21.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$reportBTM$eventHandlers$34.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$reportBTM$eventHandlers$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils$reportBTM$eventHandlers$5.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$changeMethod$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$eventHandlers$5.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$eventHandlers$6.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$eventHandlers$7.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$eventHandlers$8.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$reportAndExitCashier$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/CJUnifyPayAssetInfoUtils.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/FrontCounterProvider$startNewET$1$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/FrontCounterProvider$startNewStandard$1$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainManager$showRecommendPopup$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainManager$showRecommendPopup$2$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainManager$startQueryPayType$1$onSuccess$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainProvider.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/CreditPayVoucherViewHolder$bindData$1$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/b$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/b$e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/data/FrontPaymentMethodInfo.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment$onGetMethodListSuccess$performTask$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMainFragment$onGetMethodListSuccess$performTask$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMethodFragment$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMethodFragment$scheduleRelayoutMethodPanelAfterConfiguration$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/x.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/PayAgainMainPresenter.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/g0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/y.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/FrontMethodGroupStyleWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/FrontMethodWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/FrontMethodWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideCreditPayWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideNormalWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideVoucherHalfWrapper$initAction$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initActions$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initTitleBar$8.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$setUpOldSyleLayout$5.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/e0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSAgreementDetailFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/utils/CJPaySupplementarySignProvider.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/CJPayUIUtils.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/CreditPayProcessUtils$appendExtInfo$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/CreditPayProcessUtils$appendExtInfo$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/JumpLynxProcessUtil$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/a$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainDialogFromScene.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$businessDidEnter$reportError$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$showRetainDialog$4$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$showRetainDialog$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$showRetainDialog$subTypeList$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$showRetainDialog$subTypeList$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b$d$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b$h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/c0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/s.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/x$e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/x.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/CJPayLynxDialogUtils$buildBasicEventHandlerMap$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/CJPayVerifyHelperUtils$BubblePosition.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/NewPwdUtil.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyAgreementDetailFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyAgreementListFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyCvvCheckFragment$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyCvvCheckFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyFingerPrintPreHalfWindowFragment$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyIdentityFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyMaskFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$getLynxKeepDialogEventHandler$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$getLynxKeepDialogEventHandler$eventHandlers$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$openCreditPayActivate$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$r.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$y.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment$m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment$n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment$q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFullFragment$a$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFullFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsHelpFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/b0$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/b0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/j0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/k0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/s0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/t.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/v0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/w.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/w0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/NewVerifyDiscountWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/PwdBaseWrapper$PageType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/PwdBaseWrapper$initErrorTipsView$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/PwdBaseWrapper$initErrorTipsView$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/PwdBaseWrapper$initTopRightVerifyTextView$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/VerifyPayTypeWithCombineWrapper$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/g0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/h0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/t.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/x0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/z.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/z0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyFaceVM$buildKeepDialogConfig$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyOneStepPaymentVM$buildKeepDialogConfig$onExpanded$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyOneStepPaymentVM$keepDialogConfig$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/a$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/a$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/b0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/c0$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/e$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/e$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/f0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/h0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/i$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/i$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/i0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/j0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l1$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l1$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p0$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p0$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p1$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p1$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/s.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/v.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/x.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/x0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/y.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/view/CJBindCardConfirmDialog.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/view/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/view/wrapper/CJPayVoucherWrapper$VoucherViewHolder$TagShowType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession$doVoiceVerify$bizContentParams$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession$startRecording$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession$startRecording$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/bean/VoicePrintOperation.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/bean/VoicePrintResult$DetailCode.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/common/VoicePrintTracker$MicroAccessStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/common/VoicePrintTracker.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/AudioHelper$ensureSami$modelPath$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/AudioHelper$stopRecordInternal$2$5$invoked$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/SAMICoreDeNoise$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/j$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/VoicePrintController.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayactivity/TTCJPayTransActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/CarrierFetchScene.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtils$openH5ByScheme$1$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$antiFraudBeforePay$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$antiFraudBeforePay$2$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$antiFraudBeforePay$2$6.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$getOnPayResultCallback$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$init$1$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$init$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$openH5ByScheme$4$schema$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner$payCallSignOuterPay$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/activity/DyStepUpIFrameActivity$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/activity/DyVerifyActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/api/ICJPayDyVerifyProvider$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/api/ICJPayDyVerifyProvider.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/base/DyVerifyBaseManager$verifyCallback$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/constants/DyVerifySmsMobileType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/JSBIDaaSAuth$doLoading$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/abs/AbsJsbDyVerify$DyVerifyOutput.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/abs/AbsJsbDyVerify.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/abs/AbsJsbIDaaSAuth.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/abs/AbsJsbOperateCert.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/abs/AbsJsbVoiceVerify.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/jsb/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/utils/PrefetchIDaaSAuthHelper$prefetchForIDaaSAuth$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/utils/PrefetchIDaaSAuthHelper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/utils/i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifyCertFragment$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifyCertFragment$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifyCertFragment$initActions$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsFragment$initActions$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsFragment$onVerifySuccess$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsHelpFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/view/fragment/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$asyncGetToken$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$closeFingerprint$1$1$closeWithToken$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$processAsyncResponse$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM$showVerifyDialog$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifySmsVM.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/k.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/FqbasePreloadImageMethod$loadFromLocalPath$1.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/b.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/g.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/r.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/core/b.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/core/g.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/core/h.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/helper/AnniexPageBroadcastHelper$broadcastReceiver$1$onReceive$1.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/service/FqLynxBizService$initLynxBizService$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/service/FqLynxBizService$initLynxBizService$1$2.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/ui/view/TitleBar.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/util/ImageLoader.smali` | 0 | 0 | 1 | 1 |
| `com/by/inflate_lib/inflator/TranlateUtilKt.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/base/service/protocol/media/entity/ImageInfo.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/liveplayer/IGameTTLivePlayer$LiveError.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/liveplayer/IGameTTLivePlayer$Orientation.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/pay/model/WxGamePayParamEntity.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/permission/MglServerPermissionAuthPopupConfig$a.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/permission/MglServerPermissionModel$Companion.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/share/BdpShareBaseInfo$ShareAppInfo.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/share/ShareImCallbackInfo$Companion.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/minigame/interaction/util/InteractionSdkKt.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/service/api/strategy/StrategyManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/BdAccountSeal.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/domain/RegionType.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/sdk/ProcessResult.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/ZDataModel$anyMap$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/ZDataModel$jsonObject$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/ZDataModel.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/gip/WindMillDetailFragment$f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/XOpenMethod.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/a0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/b0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/e.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/e0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/g.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/n.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/p.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/r.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/x.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/y.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/z.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/AdModel$NativeSiteAdInfo.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/AdModel$WcMiniAppInfo.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/AdModel.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/DynamicAdData$NativeSiteAdInfo.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/enums/InteractionType$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/banner/components/d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/banner/impl/BannerAdRequestImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/banner/request/BannerRequestBase.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/inspire/impl/DownloadImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/base/component/BaseRemoteViewsService$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/base/component/BaseService$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/base/component/BaseService.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/base/component/BaseXmFgService.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/bean/WakeUpLog.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/hipc/IpcProxyImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/InstrumentationServiceImpl$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/InstrumentationServiceImpl$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a0$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/c0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/d$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/d$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/e0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/f0$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/f0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/g0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/h$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/h0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/i0$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/i0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/j0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/k.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/k0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/l0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/m0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/n0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/o$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/p0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/q0$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/q0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/r.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/r0$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/s0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/t0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/u0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/v0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/w0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/x0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/y.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/y0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/z0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/utils/Utils$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/utils/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/utils/h.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/utils/k.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adlp/components/api/utils/AdLpBlankDetector$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adlp/components/api/utils/AdLpBlankDetector.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adlp/components/impl/BaseAdLandingPageDownloader$adDownloadEventConfig$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adlp/components/impl/webkit/AdLpWebViewDelegate.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adtracker/model/C2STrackEvent.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/bridges/log/SifLog$sdkColor$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/client/components/settings/AbsAdSettingsManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/data/base/model/applink/AdAppLinkEventConfig.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/preload/sif/SifAdPreloadSessionConfig$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/preload/sif/g.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/reward/dynamicad/AbsRewardLynxFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/reward/feedback/RewardAdReportUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/bridge/BDARLynxBridgeModuleV2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/constant/ActivityTransitionAnimStyle.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/draw/DrawAdLoadMoreDispatcher$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/jsbridge/openreward/OpenRewardRequest.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/jsbridge/openreward/d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/lynx/AdLynxRenderMode.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/lynx/e.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/pitaya/RewardAdDayLevelFeatureUtils$yesterdayFeatureJSON$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/pitaya/RewardAdDayLevelFeatureUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/pitaya/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rifle/bridge/params/PlatformDataTransformerFactory.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rifle/perf/RifleAdPerfMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/api/IAdEventDepend$DefaultImpls.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/api/gecko/AdGeckoUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/api/ipc/AbsAdIpcSyncMethod.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/api/ipc/AdIpcCallRequest.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/api/ipc/AdIpcCallResponse$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/api/ipc/AdIpcCallResponse.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/advideo/AdLynxBehaviorServiceImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/advideo/ui/LynxAdVideoUI$$MethodInvoker.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/advideo/ui/LynxAdVideoUI$$PropsSetter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/advideo/ui/LynxAdVideoUI.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/gecko/AdGeckoManager$UpdateStatus.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/gecko/AdGeckoManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/AdIpcAidlService.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/AdIpcMainActivity.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/e.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/j.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/k.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/n.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/video/AdVideoSRUtils$bmfBinPath$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/video/AdVideoSRUtils$bmfCachePath$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/video/AdVideoSRUtils$lensBinPath$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/video/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/video/k.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/pitaya/AdIpcPitayaIsReadyMethod.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/screenshot/AdScreenShotMonitor$ScreenShotObserver$regex$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/screenshot/AdScreenShotMonitor$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/utils/ExtensionsKt.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/utils/StringToJsonAdapterFactory$create$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/exception/CapabilityCreateException$JSEvaluateCapabilityCreateException.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/js/JSEvaluateCapability$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceCapability$c$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceCapability$c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceProxy$release$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceProxy$webReportJson$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/core/AdLpSecManagerFactory.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/core/exception/SecManagerCreateErrorException$WebViewCastError.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/settings/ResourceProxyConfig.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/api/adlp/AdLpSecContext$isOrangeSite$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/adderive/toptext/TopTextHelper$getLandVideoBlurBitmap$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/adderive/toptext/TopTextHelper$preCalculateCoverColor$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/adderive/toptext/render/LandingVideoDecorateComponent$LandingVideoDecorateLynxUI.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/alog/Alog$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/alog/Log.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ui/ec/widget/feedback/ECFeedbackEnterView.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ui/ec/widget/photodraweeview/DragActionHelper.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ui/ec/widget/switchbutton/CustomSwitchCompat.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/util/IntToBooleanJsonAdapter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/annie/pro/ui/AnnieProFragment.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/instrumentation/interceptor/AddHeaderInterceptor.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/instrumentation/okhttp3/InterceptorImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/monitor/MonitorTool$3.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/monitor/MonitorTool$4.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/tracing/AutoPageTraceHelper.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/v2/instrumentation/FragmentTimeAgent.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/battery/dao/MonitorContentProvider.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/core/MonitorSharedPreferences.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/entity/ApiAllLocalLog.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/entity/BatteryLogEntity.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/h.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/internal/ApmDelegate$h.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/internal/ApmDelegate$n.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/perf/PerfCollectUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/perf/TemperatureDataManager$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/trace/fps/FpsTracer$c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/trace/fps/RealFpsTracer$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/FpsUtil.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/JsonUtils$JsonWriter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/Pair.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/TimeUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/consumer/slardar/send/DropDataMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/consumer/slardar/send/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/cpu/collect/c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/java_alloc/JavaAllocCollector.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/util/RomUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/util/timetask/AsyncTaskManager$InnerRunnable.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/et_verify/EventVerify$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/isolate/DataIsolateKey.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/map/api/MapSignalSource.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/monitor/MonitorKey.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/monitor/MonitorState.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/monitor/v3/impl/LatencyMonitor$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/PriorityWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$addPageDuration$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$newSession$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$removeLaunch$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$removeTerminate$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackLaunch$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackLaunch$3.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackLaunch$inserted$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackTerminate$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackTerminate$3.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackTerminate$inserted$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/EventDatabase.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/Group.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/Model$EventType.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/SessionDatabase.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/Worker$handleMissedGroups$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/i.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/p.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/q.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/s.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/t.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/r.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/v.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/w.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/util/EventsSenderUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/article/common/impression/ImpressionManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/TMProcessKillerConfigCache$Companion$repo$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/AutoStartObserver$recordFirstStartComponent$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/AutoStartReporter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/ProcessInfoPersist.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/ServiceReason.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/ServiceRedirectV2$tryRedirect$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/ServiceRedirectV2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/ServiceStickSwap$reportAppLog$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/BDInstallProvider.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/BaseWorker.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/b$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/d1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/e.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/e1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/i.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/k$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/migrate/MigrateDetectorActivity.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/w$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/w$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/x0.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$IWXOneJumpAdApi.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$d.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$e.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$j.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$b.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$c.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$d.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$e.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberNormalView$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberNormalViewForFullScreenVideo$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/IFixRefreshBottomTab$$Impl$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/IFixRefreshBottomTab.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$EdgeGravity.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$LockMode.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$State.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/MiraCastMonitor$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/pages/main/b.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/reader/ad/IAntouLine$POSITION.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/reader/ad/IAntouLine.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/reader/ad/j.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/rpc/rpc/MsgApiService$a.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/rpc/rpc/UgcApiService$a.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/rpc/rpc/UserApiService$a.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/util/BitmapUtils$FetchBitmapWithResizeCallback.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/BitmapUtils$ImageSizeType.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/BitmapUtils$SaveBitmapToFileCallback.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/BookNameType.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/util/CdnLargeImageLoader$CacheType.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/FrequencyMgr$b.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/IExtractColorHost.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/ILibraUploadApi.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/ImageLoaderUtils$w.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/ImageLoaderUtils$x.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/KeyBoardHelper$OnKeyBoardListener$-CC.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/KeyBoardHelper$OnKeyBoardListener.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/LoadImageCallback.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/PictureUtils$k.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/ToastUtils$l.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/UiConfigSetter$d.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/UiConfigSetter$e.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/UiConfigSetter$m.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/a7.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/f$c.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/f3$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/g2.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/h5.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/i2.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/k2.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/w1.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/x9$a.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/util/z7$a.smali` | 1 | 0 | 0 | 1 |
| `com/facebook/drawee/view/DraweeView$a.smali` | 0 | 0 | 1 | 1 |
| `com/facebook/drawee/view/SimpleDraweeView$f.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/update/IUpdateConfig.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/NetworkApi.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/OnDownloadStatusChangedListener$DownloadResultStatus.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/OnUpdateStatusChangedListener$UpdateResultStatus.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/OnUpdateStatusChangedListener.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/UpdateCheckerService.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/update/UpdateDialogStyle.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/UpdateService.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/b.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/c.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/d.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/e.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/f.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/update/z$a.smali` | 1 | 0 | 0 | 1 |
| `com/ss/android/videoshop/datasource/SimplePlayUrlConstructor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/fullscreen/FullScreenOperator$d.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/log/tracer/LogTracer.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/mediaview/SimpleMediaView.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/mediaview/TextureContainerLayout.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/mediaview/VideoPatchLayout.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/mediaview/d.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoshop/mediaview/e.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/fragment/a.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/fragment2/VideoLandingFragment.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/widget/bottombar/b.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/widget/bottombar/c.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/widget/bottombar/g.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/widget/bottombar/h.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/videoweb/sdk/widget/bottombar/l.smali` | 0 | 0 | 1 | 1 |
| `com/ss/bduploader/BDAbstractUpload.smali` | 0 | 0 | 1 | 1 |
| `com/ss/bduploader/BDUploadUtil.smali` | 0 | 0 | 1 | 1 |
| `com/ss/bduploader/logupload/AppLogEngineUploader$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/bduploader/smartserver/SmartVideoUploader.smali` | 0 | 0 | 1 | 1 |
| `com/ss/bduploader/util/X509Util.smali` | 0 | 0 | 1 | 1 |
| `com/ss/mediakit/medialoader/AVMDLDataLoader$MDLDownloader.smali` | 0 | 0 | 1 | 1 |
| `com/ss/mediakit/medialoader/AVMDLDataLoaderConfigure.smali` | 0 | 0 | 1 | 1 |
| `com/ss/mediakit/medialoader/AVMDLLibraryManager.smali` | 0 | 0 | 1 | 1 |
| `com/ss/mediakit/net/LocalDNS$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/mediakit/utils/AVMDLDeviceUtil.smali` | 0 | 0 | 1 | 1 |
| `com/ss/mediakit/vcnlib/X509Util.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/NativeWindow.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/TexGLUtils.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/TextureFactory.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/TextureRenderEventLogger.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/VideoOCLSRBmfPackageWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/VideoSDR2HDRWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/base/EGLExt.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/AdaptiveGradingEffect.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/BMFVQScoreOmniLite.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/FrameEvaluationEffect.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLAutoStereoScopyFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLColorCompareFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLHDR2SDRFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLLut3DFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLLutFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLSelectiveGaussianBlurFilter3.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/GLSelectiveGaussianBlurFilterOptMerge.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/HardwareBuffer2GLCopyFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/PureColorDetector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/effect/VideoSDR2HDREffect.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/fov/TileInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/texturerender/overlay/NormalClock.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/AJMediaCodec$3.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/AJSurfaceControl.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/AudioTrackPool.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/DirectBufferPool.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/StreamInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/TTPlayerConfiger.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/TTPlayerLibLoader.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/TTPlayerLibraryLoader.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/TTPlayerView$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/TTPlayerView$2.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/player/TTPlayerViewHelper$Size.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/utils/AVLogger.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttm/utils/HardWareInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/CDNTuningParamManger.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/DataLoaderHelper$DataLoaderTaskLoadProgress.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/MediaPlayerWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTNetWorkListener$TTPhoneStateListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$5.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$MyDNSCompletionListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$MyFrameMetadataListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$TTVideoEngineLooperThread2$MessageHandler.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$TTVideoEngineLooperThread2$MyMainLooperHandler.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineImpl$TTVideoEngineLooperThread2.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineMonitor$CrosstalkReceiver.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/TTVideoEngineMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/VideoModelCache.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/fetcher/FetcherApiHelper.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/fetcher/FetcherMaker.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/fetcher/MDLFetcher.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/fetcher/mdlfethcer/FetcherMakerNew.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/fetcher/mdlfethcer/MDLFetcherNew.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/BrightnessMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/EngineOptionCollector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/HeadsetStateMonitor$HeadsetReceiver.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/PortraitNetworkScore$NetworkQualityAlgorithmV1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/SamplingManager.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/VegaCollector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/VideoEventAbrEvent.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/VideoEventLoggerV2$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/VideoEventOneError.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/VideoFilterMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/log/ViewSizeMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/model/BareVideoInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/model/IntertrustDrmHelper$MyNetworkListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/model/LiveVideoRef.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/model/SubInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/model/VideoAdRef.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/model/VideoRef.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/net/DNSServerIP$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/net/LocalDNS$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/net/TTHTTPNetwork$2.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/net/TTHTTPNetwork.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/portrait/PortraitEngine.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/preload/PreloadModelMedia.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/preload/PreloadUtil.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/selector/gracie/GracieSelector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/selector/strategy/GearStrategyABR.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/selector/strategy/GearStrategyConfig.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/setting/SettingsHelper$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/setting/SettingsHelper$2.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/source/strategy/CodecStrategyAdapter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/source/strategy/SmartUrlFetcher.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/strategrycenter/StrategyEvent$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/strategrycenter/StrategyHelper$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/superresolution/SRStrategy.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/superresolution/SRStrategyConfig.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/utils/SntpClient.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/utils/TTVideoEngineUtils.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ttvideoengine/utils/Utils.smali` | 0 | 0 | 1 | 1 |
| `com/ss/ugc/clientai/core/api/FeatureProducer.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/LiveIOWrapper$LiveIOHandler.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/LiveIOWrapper$SysInfoSyncRunner.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/ttquic/TTEngineParam.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/ttquic/TTLogManager.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/ttquic/X509Util.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/LiveConfigKey.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/MyInvocationHandler.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VLDNSParseModel$DNSParserData.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$6.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$MyErrorListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$MyInfoListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$MyRetryListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$PlayCacheSyncRunner.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$RtcNetworkFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/abr/ABRSwitchController.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/config/PlayerStrategyConfig.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/function/AdaptiveGrading.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/function/SEIReportMgr.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/liveio/LiveIO.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/log/LineSwitcherOnRenderStall.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/model/LivePullData.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/network/DnsHelper$3.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/network/DnsHelper.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/network/NetUtils.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/retry/RetryProcessor$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/utils/URLBuilder.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/loader/MuteApplication.smali` | 0 | 0 | 1 | 1 |
| `d60/a.smali` | 0 | 0 | 1 | 1 |
| `d70/a$a.smali` | 0 | 0 | 1 | 1 |
| `d70/b$b.smali` | 0 | 0 | 1 | 1 |
| `dd/c$a.smali` | 0 | 0 | 1 | 1 |
| `dd/c.smali` | 0 | 0 | 1 | 1 |
| `di/b.smali` | 0 | 0 | 1 | 1 |
| `di/d.smali` | 0 | 0 | 1 | 1 |
| `di/h.smali` | 0 | 0 | 1 | 1 |
| `dj/c$a.smali` | 0 | 0 | 1 | 1 |
| `dl/a.smali` | 0 | 0 | 1 | 1 |
| `dl/a0.smali` | 0 | 0 | 1 | 1 |
| `dl/b.smali` | 0 | 0 | 1 | 1 |
| `dl/c.smali` | 0 | 0 | 1 | 1 |
| `dl/c0.smali` | 0 | 0 | 1 | 1 |
| `dl/e0.smali` | 0 | 0 | 1 | 1 |
| `dl/f0.smali` | 0 | 0 | 1 | 1 |
| `dl/g.smali` | 0 | 0 | 1 | 1 |
| `dl/h0.smali` | 0 | 0 | 1 | 1 |
| `dl/j.smali` | 0 | 0 | 1 | 1 |
| `dl/k.smali` | 0 | 0 | 1 | 1 |
| `dl/l.smali` | 0 | 0 | 1 | 1 |
| `dl/m.smali` | 0 | 0 | 1 | 1 |
| `dl/n.smali` | 0 | 0 | 1 | 1 |
| `dl/o.smali` | 0 | 0 | 1 | 1 |
| `dl/p.smali` | 0 | 0 | 1 | 1 |
| `dl/q.smali` | 0 | 0 | 1 | 1 |
| `dl/s.smali` | 0 | 0 | 1 | 1 |
| `dl/t.smali` | 0 | 0 | 1 | 1 |
| `dl/u.smali` | 0 | 0 | 1 | 1 |
| `dl/v.smali` | 0 | 0 | 1 | 1 |
| `dl/y.smali` | 0 | 0 | 1 | 1 |
| `dl/z.smali` | 0 | 0 | 1 | 1 |
| `do/a.smali` | 0 | 0 | 1 | 1 |
| `do/e$b.smali` | 0 | 0 | 1 | 1 |
| `do/e.smali` | 0 | 0 | 1 | 1 |
| `dq/a.smali` | 0 | 0 | 1 | 1 |
| `dr/a.smali` | 0 | 0 | 1 | 1 |
| `dr/d.smali` | 0 | 0 | 1 | 1 |
| `e30/a.smali` | 0 | 0 | 1 | 1 |
| `e30/c.smali` | 0 | 0 | 1 | 1 |
| `e30/d.smali` | 0 | 0 | 1 | 1 |
| `e60/a.smali` | 0 | 0 | 1 | 1 |
| `e8/c$b.smali` | 0 | 0 | 1 | 1 |
| `e8/c$c.smali` | 0 | 0 | 1 | 1 |
| `e8/d.smali` | 0 | 0 | 1 | 1 |
| `e80/a0.smali` | 0 | 0 | 1 | 1 |
| `e80/b0.smali` | 0 | 0 | 1 | 1 |
| `e80/c0.smali` | 0 | 0 | 1 | 1 |
| `e80/p.smali` | 0 | 0 | 1 | 1 |
| `e80/s.smali` | 0 | 0 | 1 | 1 |
| `e80/t.smali` | 0 | 0 | 1 | 1 |
| `e80/w.smali` | 0 | 0 | 1 | 1 |
| `e80/x.smali` | 0 | 0 | 1 | 1 |
| `ea/b.smali` | 0 | 0 | 1 | 1 |
| `eh/a.smali` | 0 | 0 | 1 | 1 |
| `eh/b.smali` | 0 | 0 | 1 | 1 |
| `eh/c.smali` | 0 | 0 | 1 | 1 |
| `eh/g.smali` | 0 | 0 | 1 | 1 |
| `eh/i.smali` | 0 | 0 | 1 | 1 |
| `eh/j.smali` | 0 | 0 | 1 | 1 |
| `eh/o.smali` | 0 | 0 | 1 | 1 |
| `el/b$a.smali` | 0 | 0 | 1 | 1 |
| `el/b.smali` | 0 | 0 | 1 | 1 |
| `el/c.smali` | 0 | 0 | 1 | 1 |
| `el/d.smali` | 0 | 0 | 1 | 1 |
| `eq/a.smali` | 0 | 0 | 1 | 1 |
| `eq/b$a.smali` | 0 | 0 | 1 | 1 |
| `f50/c.smali` | 0 | 0 | 1 | 1 |
| `f70/c.smali` | 0 | 0 | 1 | 1 |
| `f70/d.smali` | 0 | 0 | 1 | 1 |
| `f70/k.smali` | 0 | 0 | 1 | 1 |
| `fb/c.smali` | 0 | 0 | 1 | 1 |
| `fb/f.smali` | 0 | 0 | 1 | 1 |
| `fb/h.smali` | 0 | 0 | 1 | 1 |
| `fi/b.smali` | 0 | 0 | 1 | 1 |
| `fk/d.smali` | 0 | 0 | 1 | 1 |
| `fk/g$c.smali` | 0 | 0 | 1 | 1 |
| `fo/c.smali` | 0 | 0 | 1 | 1 |
| `fo/d.smali` | 0 | 0 | 1 | 1 |
| `fo/e.smali` | 0 | 0 | 1 | 1 |
| `fo/f.smali` | 0 | 0 | 1 | 1 |
| `fo/g.smali` | 0 | 0 | 1 | 1 |
| `g40/a.smali` | 0 | 0 | 1 | 1 |
| `g60/a.smali` | 0 | 0 | 1 | 1 |
| `g60/b.smali` | 0 | 0 | 1 | 1 |
| `g60/g.smali` | 0 | 0 | 1 | 1 |
| `g60/i.smali` | 0 | 0 | 1 | 1 |
| `g60/k.smali` | 0 | 0 | 1 | 1 |
| `g8/f.smali` | 0 | 0 | 1 | 1 |
| `g8/h$a.smali` | 0 | 0 | 1 | 1 |
| `g8/i.smali` | 0 | 0 | 1 | 1 |
| `g8/j.smali` | 0 | 0 | 1 | 1 |
| `g9/e.smali` | 0 | 0 | 1 | 1 |
| `gb/a.smali` | 0 | 0 | 1 | 1 |
| `gc/b.smali` | 0 | 0 | 1 | 1 |
| `gg/h.smali` | 0 | 0 | 1 | 1 |
| `gg/i.smali` | 0 | 0 | 1 | 1 |
| `gk/a.smali` | 0 | 0 | 1 | 1 |
| `gm/e.smali` | 0 | 0 | 1 | 1 |
| `gr/c.smali` | 0 | 0 | 1 | 1 |
| `h20/a.smali` | 0 | 0 | 1 | 1 |
| `h60/a.smali` | 0 | 0 | 1 | 1 |
| `h70/e.smali` | 0 | 0 | 1 | 1 |
| `h70/k.smali` | 0 | 0 | 1 | 1 |
| `h70/m.smali` | 0 | 0 | 1 | 1 |
| `hc/a.smali` | 0 | 0 | 1 | 1 |
| `hh/b.smali` | 0 | 0 | 1 | 1 |
| `hh/g.smali` | 0 | 0 | 1 | 1 |
| `hi/a.smali` | 0 | 0 | 1 | 1 |
| `hi/b.smali` | 0 | 0 | 1 | 1 |
| `hk/b$a.smali` | 0 | 0 | 1 | 1 |
| `hk/c$b.smali` | 0 | 0 | 1 | 1 |
| `hl/a.smali` | 0 | 0 | 1 | 1 |
| `hl/b.smali` | 0 | 0 | 1 | 1 |
| `hl/c.smali` | 0 | 0 | 1 | 1 |
| `hl/e.smali` | 0 | 0 | 1 | 1 |
| `hl/f.smali` | 0 | 0 | 1 | 1 |
| `hn/d.smali` | 0 | 0 | 1 | 1 |
| `i20/a.smali` | 0 | 0 | 1 | 1 |
| `i30/b.smali` | 0 | 0 | 1 | 1 |
| `ia/d.smali` | 0 | 0 | 1 | 1 |
| `ia/e.smali` | 0 | 0 | 1 | 1 |
| `ia/f.smali` | 0 | 0 | 1 | 1 |
| `ia/h.smali` | 0 | 0 | 1 | 1 |
| `ia/j.smali` | 0 | 0 | 1 | 1 |
| `ia/k.smali` | 0 | 0 | 1 | 1 |
| `ib/a$a.smali` | 0 | 0 | 1 | 1 |
| `ih/b$b.smali` | 0 | 0 | 1 | 1 |
| `ih/b.smali` | 0 | 0 | 1 | 1 |
| `ih/c.smali` | 0 | 0 | 1 | 1 |
| `ih/g.smali` | 0 | 0 | 1 | 1 |
| `ih/h.smali` | 0 | 0 | 1 | 1 |
| `ii/a.smali` | 0 | 0 | 1 | 1 |
| `ii/e.smali` | 0 | 0 | 1 | 1 |
| `ik/a.smali` | 0 | 0 | 1 | 1 |
| `ik/c.smali` | 0 | 0 | 1 | 1 |
| `in/d.smali` | 0 | 0 | 1 | 1 |
| `ip/c.smali` | 0 | 0 | 1 | 1 |
| `j40/e.smali` | 0 | 0 | 1 | 1 |
| `j50/a.smali` | 0 | 0 | 1 | 1 |
| `jb/b.smali` | 0 | 0 | 1 | 1 |
| `jb/d.smali` | 0 | 0 | 1 | 1 |
| `jb/e.smali` | 0 | 0 | 1 | 1 |
| `jb/l.smali` | 0 | 0 | 1 | 1 |
| `jb/r.smali` | 0 | 0 | 1 | 1 |
| `jb/t.smali` | 0 | 0 | 1 | 1 |
| `jb/v.smali` | 0 | 0 | 1 | 1 |
| `jb/x.smali` | 0 | 0 | 1 | 1 |
| `jg/a$a.smali` | 0 | 0 | 1 | 1 |
| `jk/b.smali` | 0 | 0 | 1 | 1 |
| `jm/a.smali` | 0 | 0 | 1 | 1 |
| `jo/a$b.smali` | 0 | 0 | 1 | 1 |
| `k40/d.smali` | 0 | 0 | 1 | 1 |
| `ka/d.smali` | 0 | 0 | 1 | 1 |
| `kc/e.smali` | 0 | 0 | 1 | 1 |
| `kc/f.smali` | 0 | 0 | 1 | 1 |
| `ke/d.smali` | 0 | 0 | 1 | 1 |
| `ki/c.smali` | 0 | 0 | 1 | 1 |
| `kk/d$b.smali` | 0 | 0 | 1 | 1 |
| `kk/f.smali` | 0 | 0 | 1 | 1 |
| `kn/e.smali` | 0 | 0 | 1 | 1 |
| `kn/h.smali` | 0 | 0 | 1 | 1 |
| `l20/a.smali` | 0 | 0 | 1 | 1 |
| `l40/b.smali` | 0 | 0 | 1 | 1 |
| `l40/f.smali` | 0 | 0 | 1 | 1 |
| `l60/a.smali` | 0 | 0 | 1 | 1 |
| `la/b.smali` | 0 | 0 | 1 | 1 |
| `la/c.smali` | 0 | 0 | 1 | 1 |
| `lb/d.smali` | 0 | 0 | 1 | 1 |
| `lb/e.smali` | 0 | 0 | 1 | 1 |
| `lc/l$a.smali` | 0 | 0 | 1 | 1 |
| `lc/n.smali` | 0 | 0 | 1 | 1 |
| `lc/u$a.smali` | 0 | 0 | 1 | 1 |
| `lc/w.smali` | 0 | 0 | 1 | 1 |
| `lc/y.smali` | 0 | 0 | 1 | 1 |
| `li/a.smali` | 0 | 0 | 1 | 1 |
| `lk/a$b.smali` | 0 | 0 | 1 | 1 |
| `ll/a$b.smali` | 0 | 0 | 1 | 1 |
| `ll/b.smali` | 0 | 0 | 1 | 1 |
| `ma/a.smali` | 0 | 0 | 1 | 1 |
| `ma/b.smali` | 0 | 0 | 1 | 1 |
| `mb/a.smali` | 0 | 0 | 1 | 1 |
| `mb/f.smali` | 0 | 0 | 1 | 1 |
| `mb/w.smali` | 0 | 0 | 1 | 1 |
| `mb/x.smali` | 0 | 0 | 1 | 1 |
| `mf/c.smali` | 0 | 0 | 1 | 1 |
| `mk/a$a$a.smali` | 0 | 0 | 1 | 1 |
| `mn/c.smali` | 0 | 0 | 1 | 1 |
| `n40/c.smali` | 0 | 0 | 1 | 1 |
| `n40/d.smali` | 0 | 0 | 1 | 1 |
| `n9/a.smali` | 0 | 0 | 1 | 1 |
| `na/a.smali` | 0 | 0 | 1 | 1 |
| `nc/a.smali` | 0 | 0 | 1 | 1 |
| `nd/d.smali` | 0 | 0 | 1 | 1 |
| `nd/f.smali` | 0 | 0 | 1 | 1 |
| `nd/g.smali` | 0 | 0 | 1 | 1 |
| `nd/i.smali` | 0 | 0 | 1 | 1 |
| `nf/a.smali` | 0 | 0 | 1 | 1 |
| `nh/f.smali` | 0 | 0 | 1 | 1 |
| `nk/a$b$a$a.smali` | 0 | 0 | 1 | 1 |
| `nk/b.smali` | 0 | 0 | 1 | 1 |
| `nk/c.smali` | 0 | 0 | 1 | 1 |
| `nk/d.smali` | 0 | 0 | 1 | 1 |
| `nq/a$a.smali` | 0 | 0 | 1 | 1 |
| `o20/c.smali` | 0 | 0 | 1 | 1 |
| `o40/c.smali` | 0 | 0 | 1 | 1 |
| `o60/a.smali` | 0 | 0 | 1 | 1 |
| `od/k.smali` | 0 | 0 | 1 | 1 |
| `oe/d.smali` | 0 | 0 | 1 | 1 |
| `oe/e$a.smali` | 0 | 0 | 1 | 1 |
| `oe/f.smali` | 0 | 0 | 1 | 1 |
| `og/a.smali` | 0 | 0 | 1 | 1 |
| `oi/a.smali` | 0 | 0 | 1 | 1 |
| `oi/b$a.smali` | 0 | 0 | 1 | 1 |
| `ok/a.smali` | 0 | 0 | 1 | 1 |
| `ol/b.smali` | 0 | 0 | 1 | 1 |
| `om/d.smali` | 0 | 0 | 1 | 1 |
| `oq/a$a.smali` | 0 | 0 | 1 | 1 |
| `oq/g$a.smali` | 0 | 0 | 1 | 1 |
| `p20/a.smali` | 0 | 0 | 1 | 1 |
| `p60/c.smali` | 0 | 0 | 1 | 1 |
| `p60/k$a.smali` | 0 | 0 | 1 | 1 |
| `p60/m.smali` | 0 | 0 | 1 | 1 |
| `p8/a$a.smali` | 0 | 0 | 1 | 1 |
| `p8/a.smali` | 0 | 0 | 1 | 1 |
| `p8/e.smali` | 0 | 0 | 1 | 1 |
| `p8/g.smali` | 0 | 0 | 1 | 1 |
| `p8/i.smali` | 0 | 0 | 1 | 1 |
| `p8/j.smali` | 0 | 0 | 1 | 1 |
| `p8/n.smali` | 0 | 0 | 1 | 1 |
| `p8/q$a.smali` | 0 | 0 | 1 | 1 |
| `p8/q.smali` | 0 | 0 | 1 | 1 |
| `ph/k.smali` | 0 | 0 | 1 | 1 |
| `pk/f$a.smali` | 0 | 0 | 1 | 1 |
| `pk/g.smali` | 0 | 0 | 1 | 1 |
| `pl/a.smali` | 0 | 0 | 1 | 1 |
| `pp/a.smali` | 0 | 0 | 1 | 1 |
| `pp/b.smali` | 0 | 0 | 1 | 1 |
| `pq/a.smali` | 0 | 0 | 1 | 1 |
| `q20/b.smali` | 0 | 0 | 1 | 1 |
| `q20/c.smali` | 0 | 0 | 1 | 1 |
| `q20/f.smali` | 0 | 0 | 1 | 1 |
| `q20/g.smali` | 0 | 0 | 1 | 1 |
| `q20/h$a$a.smali` | 0 | 0 | 1 | 1 |
| `q20/h$a.smali` | 0 | 0 | 1 | 1 |
| `q20/h.smali` | 0 | 0 | 1 | 1 |
| `q20/j.smali` | 0 | 0 | 1 | 1 |
| `q30/b.smali` | 0 | 0 | 1 | 1 |
| `q30/d.smali` | 0 | 0 | 1 | 1 |
| `q30/f$a.smali` | 0 | 0 | 1 | 1 |
| `q30/f$b.smali` | 0 | 0 | 1 | 1 |
| `q30/f$d.smali` | 0 | 0 | 1 | 1 |
| `q30/f.smali` | 0 | 0 | 1 | 1 |
| `q40/a.smali` | 0 | 0 | 1 | 1 |
| `q60/b$a.smali` | 0 | 0 | 1 | 1 |
| `q60/b.smali` | 0 | 0 | 1 | 1 |
| `qb/a.smali` | 0 | 0 | 1 | 1 |
| `qe/b.smali` | 0 | 0 | 1 | 1 |
| `qe/c$a.smali` | 0 | 0 | 1 | 1 |
| `qf/a.smali` | 0 | 0 | 1 | 1 |
| `qf/e.smali` | 0 | 0 | 1 | 1 |
| `qi/a.smali` | 0 | 0 | 1 | 1 |
| `qi/b.smali` | 0 | 0 | 1 | 1 |
| `qi/d$e$b.smali` | 0 | 0 | 1 | 1 |
| `qn/c.smali` | 0 | 0 | 1 | 1 |
| `r40/b.smali` | 0 | 0 | 1 | 1 |
| `r40/h.smali` | 0 | 0 | 1 | 1 |
| `rb/c.smali` | 0 | 0 | 1 | 1 |
| `rd/b.smali` | 0 | 0 | 1 | 1 |
| `ri/a$b$a.smali` | 0 | 0 | 1 | 1 |
| `ri/a$b.smali` | 0 | 0 | 1 | 1 |
| `ri/c$a.smali` | 0 | 0 | 1 | 1 |
| `rl/a.smali` | 0 | 0 | 1 | 1 |
| `rl/b.smali` | 0 | 0 | 1 | 1 |
| `rp/c.smali` | 0 | 0 | 1 | 1 |
| `sb/c.smali` | 0 | 0 | 1 | 1 |
| `sb/d.smali` | 0 | 0 | 1 | 1 |
| `sc/a$e.smali` | 0 | 0 | 1 | 1 |
| `sc/b.smali` | 0 | 0 | 1 | 1 |
| `sf/a$a.smali` | 0 | 0 | 1 | 1 |
| `si/c.smali` | 0 | 0 | 1 | 1 |
| `sj/a.smali` | 0 | 0 | 1 | 1 |
| `sj/b.smali` | 0 | 0 | 1 | 1 |
| `sj/g.smali` | 0 | 0 | 1 | 1 |
| `sk/e.smali` | 0 | 0 | 1 | 1 |
| `sq/h.smali` | 0 | 0 | 1 | 1 |
| `t30/h.smali` | 0 | 0 | 1 | 1 |
| `t30/j.smali` | 0 | 0 | 1 | 1 |
| `t40/a$a.smali` | 0 | 0 | 1 | 1 |
| `t40/a.smali` | 0 | 0 | 1 | 1 |
| `t40/c$a.smali` | 0 | 0 | 1 | 1 |
| `t40/c$b.smali` | 0 | 0 | 1 | 1 |
| `t40/c$d.smali` | 0 | 0 | 1 | 1 |
| `tf/c.smali` | 0 | 0 | 1 | 1 |
| `tg/a.smali` | 0 | 0 | 1 | 1 |
| `tg/b.smali` | 0 | 0 | 1 | 1 |
| `tg/c.smali` | 0 | 0 | 1 | 1 |
| `tg/f.smali` | 0 | 0 | 1 | 1 |
| `tg/j.smali` | 0 | 0 | 1 | 1 |
| `tg/n.smali` | 0 | 0 | 1 | 1 |
| `tg/o.smali` | 0 | 0 | 1 | 1 |
| `ti/a.smali` | 0 | 0 | 1 | 1 |
| `tj/a$f.smali` | 0 | 0 | 1 | 1 |
| `tj/a$j.smali` | 0 | 0 | 1 | 1 |
| `tj/c.smali` | 0 | 0 | 1 | 1 |
| `tj/f$b.smali` | 0 | 0 | 1 | 1 |
| `tj/i.smali` | 0 | 0 | 1 | 1 |
| `tj/j.smali` | 0 | 0 | 1 | 1 |
| `tm/c.smali` | 0 | 0 | 1 | 1 |
| `tq/c.smali` | 0 | 0 | 1 | 1 |
| `u60/b.smali` | 0 | 0 | 1 | 1 |
| `u9/a$a.smali` | 0 | 0 | 1 | 1 |
| `u9/b$a.smali` | 0 | 0 | 1 | 1 |
| `u9/e.smali` | 0 | 0 | 1 | 1 |
| `ua/b.smali` | 0 | 0 | 1 | 1 |
| `ui/b.smali` | 0 | 0 | 1 | 1 |
| `ui/c.smali` | 0 | 0 | 1 | 1 |
| `ui/e.smali` | 0 | 0 | 1 | 1 |
| `ui/g.smali` | 0 | 0 | 1 | 1 |
| `ui/j$a.smali` | 0 | 0 | 1 | 1 |
| `uj/a.smali` | 0 | 0 | 1 | 1 |
| `uj/d.smali` | 0 | 0 | 1 | 1 |
| `v20/b.smali` | 0 | 0 | 1 | 1 |
| `v20/c.smali` | 0 | 0 | 1 | 1 |
| `v40/b.smali` | 0 | 0 | 1 | 1 |
| `v70/d.smali` | 0 | 0 | 1 | 1 |
| `v9/a.smali` | 0 | 0 | 1 | 1 |
| `vb/f$a.smali` | 0 | 0 | 1 | 1 |
| `vc/a.smali` | 0 | 0 | 1 | 1 |
| `vc/b.smali` | 0 | 0 | 1 | 1 |
| `vf/a.smali` | 0 | 0 | 1 | 1 |
| `vf/f.smali` | 0 | 0 | 1 | 1 |
| `w20/d.smali` | 0 | 0 | 1 | 1 |
| `w20/h.smali` | 0 | 0 | 1 | 1 |
| `w20/j.smali` | 0 | 0 | 1 | 1 |
| `w30/e.smali` | 0 | 0 | 1 | 1 |
| `w30/f.smali` | 0 | 0 | 1 | 1 |
| `w60/f.smali` | 0 | 0 | 1 | 1 |
| `w60/g.smali` | 0 | 0 | 1 | 1 |
| `wd/b$e.smali` | 0 | 0 | 1 | 1 |
| `wi/b.smali` | 0 | 0 | 1 | 1 |
| `wi/d.smali` | 0 | 0 | 1 | 1 |
| `wi/e.smali` | 0 | 0 | 1 | 1 |
| `wi/f$a.smali` | 0 | 0 | 1 | 1 |
| `wj/b$a.smali` | 0 | 0 | 1 | 1 |
| `wj/b$d.smali` | 0 | 0 | 1 | 1 |
| `wj/b$e.smali` | 0 | 0 | 1 | 1 |
| `wp/a.smali` | 0 | 0 | 1 | 1 |
| `x20/a.smali` | 0 | 0 | 1 | 1 |
| `x20/c.smali` | 0 | 0 | 1 | 1 |
| `x20/d.smali` | 0 | 0 | 1 | 1 |
| `x60/a.smali` | 0 | 0 | 1 | 1 |
| `x60/c.smali` | 0 | 0 | 1 | 1 |
| `x60/d$a.smali` | 0 | 0 | 1 | 1 |
| `x9/a.smali` | 0 | 0 | 1 | 1 |
| `xc/b.smali` | 0 | 0 | 1 | 1 |
| `xc/e$d.smali` | 0 | 0 | 1 | 1 |
| `xc/e$g.smali` | 0 | 0 | 1 | 1 |
| `xc/e$h.smali` | 0 | 0 | 1 | 1 |
| `xc/f.smali` | 0 | 0 | 1 | 1 |
| `xc/g.smali` | 0 | 0 | 1 | 1 |
| `xc/h.smali` | 0 | 0 | 1 | 1 |
| `xe/c$a.smali` | 0 | 0 | 1 | 1 |
| `xe/f$a.smali` | 0 | 0 | 1 | 1 |
| `xe/f.smali` | 0 | 0 | 1 | 1 |
| `xf/a$a.smali` | 0 | 0 | 1 | 1 |
| `xf/a.smali` | 0 | 0 | 1 | 1 |
| `xf/h$a.smali` | 0 | 0 | 1 | 1 |
| `xf/h.smali` | 0 | 0 | 1 | 1 |
| `xh/h.smali` | 0 | 0 | 1 | 1 |
| `xj/a.smali` | 0 | 0 | 1 | 1 |
| `y20/a.smali` | 0 | 0 | 1 | 1 |
| `y40/a.smali` | 0 | 0 | 1 | 1 |
| `yb/c.smali` | 0 | 0 | 1 | 1 |
| `yb3/a.smali` | 0 | 0 | 1 | 1 |
| `yc/b.smali` | 0 | 0 | 1 | 1 |
| `yc/d.smali` | 0 | 0 | 1 | 1 |
| `ye/a.smali` | 0 | 0 | 1 | 1 |
| `ye/d.smali` | 0 | 0 | 1 | 1 |
| `yf/e.smali` | 0 | 0 | 1 | 1 |
| `yk/a.smali` | 0 | 0 | 1 | 1 |
| `yn/a.smali` | 0 | 0 | 1 | 1 |
| `yp/h.smali` | 0 | 0 | 1 | 1 |
| `yq/a.smali` | 0 | 0 | 1 | 1 |
| `z20/e$b.smali` | 0 | 0 | 1 | 1 |
| `z20/e.smali` | 0 | 0 | 1 | 1 |
| `z20/m.smali` | 0 | 0 | 1 | 1 |
| `z30/a.smali` | 0 | 0 | 1 | 1 |
| `z40/a$a.smali` | 0 | 0 | 1 | 1 |
| `z50/c.smali` | 0 | 0 | 1 | 1 |
| `z8/b.smali` | 0 | 0 | 1 | 1 |
| `za/a.smali` | 0 | 0 | 1 | 1 |
| `zb/c.smali` | 0 | 0 | 1 | 1 |
| `zd/c$a.smali` | 0 | 0 | 1 | 1 |
| `zi/c$a.smali` | 0 | 0 | 1 | 1 |
| `zn/b.smali` | 0 | 0 | 1 | 1 |
| `zn/c.smali` | 0 | 0 | 1 | 1 |

## 4. 真删除类清单

（无——破解者未删除任何官方类，与番茄 16a 行为一致）

## 5. dex 挪位对照（重打包证据，无语义）

- 同名类在 mod/inner 都出现且来源 dex 不同的数量（挪位规模，信息项）: 类名对齐总数 289416

## 6. 归档结构

```
hg3-diff-baksmali/
├── added/    真新增类 baksmali 全文
├── changed/  修改类差异方法全文（三段标注）
└── removed/  删除类 inner 全文
```

## 7. 与番茄 round16a 壳类画像重合分析

> 口径：主类名归一（`X$a`/`X$1` → `X`），红果真新增类 × 番茄 16a 真新增 1249 类画像。
> 红果真新增 1228 个 .smali 文件 = 归一后 **1218 主类**；画像基线 1249 归一 1213 主类。

### ★ 公共类重合率 = 1125 / 1218 = **92.4%** （≥30%，未触红旗）

### 重合类按包分组（A 类候选：壳代码）

| 包前缀 | 类数 |
|---|---|
| `com/` | 1081 |
| `org/checkerframework/` | 33 |
| `org/lsposed/` | 6 |
| `com/pandora/` | 3 |
| `sgcore0/` | 1 |
| `sgcore0/hidden/` | 1 |

### 红果独有类按包分组（B/C/D 类候选——番茄壳中不存在）

| 包前缀 | 类数 |
|---|---|
| `com/dragon/` | 77 |
| `an2/` | 9 |
| `com/pandora/` | 3 |
| `com/ss/` | 2 |
| `com/b/` | 1 |
| `com/` | 1 |

### 红果独有类完整清单

```
an2/۟ۡۧۤۧ
an2/۟ۢۢ۠ۦ
an2/۟ۦۧۤ۟
an2/۟ۦۨۢۤ
an2/ۡۥ۠ۦ
an2/ۥۣۣۢ
an2/ۦۥۣ
an2/ۧۢۧ۠
an2/ۧۥۥۤ
com/b/a
com/dragon/read/ad/util/۟ۢۢۤۤ
com/dragon/read/ad/util/۟ۥۡۤۧ
com/dragon/read/ad/util/۠۟ۦۤ
com/dragon/read/ad/util/۠ۥۣ۟
com/dragon/read/ad/util/ۡ۟ۤۢ
com/dragon/read/ad/util/ۢۥۥۥ
com/dragon/read/ad/util/ۢۧۦۦ
com/dragon/read/ad/util/ۣۢۨۢ
com/dragon/read/ad/util/ۦۨ۠ۥ
com/dragon/read/ad/util/ۧۤ۠۠
com/dragon/read/ad/util/ۧۦۤۤ
com/dragon/read/base/ssconfig/model/۟۠ۨۨ۟
com/dragon/read/base/ssconfig/model/۟ۡ۠ۧۢ
com/dragon/read/base/ssconfig/model/ۣۣ۟۠۟
com/dragon/read/base/ssconfig/model/ۣۣ۟ۤۨ
com/dragon/read/base/ssconfig/model/۟ۦۤ۠۟
com/dragon/read/base/ssconfig/model/ۤۨ۟۠
com/dragon/read/base/ssconfig/model/ۥۦۥۦ
com/dragon/read/base/ssconfig/model/ۦۤۨۦ
com/dragon/read/component/biz/impl/mine/card/model/ۣ۟۠۠ۨ
com/dragon/read/component/biz/impl/mine/card/model/۟ۤۡۨ۟
com/dragon/read/component/biz/impl/mine/card/model/۠ۢۦ۠
com/dragon/read/component/biz/impl/mine/card/model/ۢۥۡ
com/dragon/read/component/biz/impl/mine/card/model/ۣۤۨ۟
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣ۟ۢ۟
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣ۟ۤۦۧ
com/dragon/read/component/biz/impl/mine/loginv2/view/۠۠ۥۡ
com/dragon/read/component/biz/impl/mine/loginv2/view/۠ۥۡۡ
com/dragon/read/component/biz/impl/mine/loginv2/view/ۢ۟ۦ۟
com/dragon/read/component/biz/impl/mine/loginv2/view/ۢۥۦۨ
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣۨ
com/dragon/read/component/biz/impl/mine/۠ۡ
com/dragon/read/pages/main/ۣ۟ۡۥۤ
com/dragon/read/pages/main/۟ۧۦ۟ۥ
com/dragon/read/pages/main/ۤۢۨ
com/dragon/read/pages/main/ۣۤۤۨ
com/dragon/read/pages/main/ۤۦ۟ۡ
com/dragon/read/pages/main/ۤۦۦۧ
com/dragon/read/pages/main/ۧۨۦۦ
com/dragon/read/polaris/۟ۡ۠ۢۧ
com/dragon/read/polaris/۟ۢۦۦ
com/dragon/read/polaris/۟ۧۢۥۨ
com/dragon/read/polaris/ۡ۟ۢۡ
com/dragon/read/polaris/ۣۢۧۨ
com/dragon/read/polaris/ۤۥ۠ۨ
com/dragon/read/polaris/ۧ۟ۡ۠
com/dragon/read/polaris/ۨ۟۟ۡ
com/dragon/read/reader/ad/noad/۟ۥۣۡۦ
com/dragon/read/reader/ad/noad/۟ۧۡۧۤ
com/dragon/read/reader/ad/noad/۟ۧۤۦۢ
com/dragon/read/reader/ad/noad/ۡۦۧۡ
com/dragon/read/reader/ad/noad/ۣۣۤۨ
com/dragon/read/reader/ad/noad/ۦۢ۟ۡ
com/dragon/read/reader/ad/۟ۡ۠ۧ۟
com/dragon/read/reader/ad/۟ۤۡۢ۟
com/dragon/read/reader/ad/ۡۡۤ۟
com/dragon/read/reader/ad/ۣ۟ۦ۟
com/dragon/read/reader/ad/ۥۢۨۡ
com/dragon/read/reader/ad/ۧ۟۟ۦ
com/dragon/read/reader/ad/ۣۨۢۧ
com/dragon/read/rpc/rpc/۟۟ۥۢ۠
com/dragon/read/rpc/rpc/۟ۧۡ۠ۦ
com/dragon/read/rpc/rpc/ۣۥۢۡ
com/dragon/read/user/model/۟۠۟۟ۡ
com/dragon/read/user/model/۟۠ۤۧ۠
com/dragon/read/user/model/۟ۡ۟۟ۨ
com/dragon/read/user/model/۟ۢۦۥۨ
com/dragon/read/user/model/۟ۧۤ۠ۤ
com/dragon/read/user/model/۟ۧۦۦۦ
com/dragon/read/user/model/ۣ۟ۥ۠
com/dragon/read/user/model/ۤۢۢۧ
com/dragon/read/util/۟۟۟ۧ۟
com/dragon/read/util/ۣ۟ۢۢ۟
com/dragon/read/util/ۣ۟ۤ۟ۧ
com/dragon/read/util/۠ۤۦ۠
com/dragon/read/util/ۢۡ۟ۦ
com/dragon/read/util/ۥ۠ۧۢ
com/pandora/core/۟۠ۥۧ۟
com/pandora/core/ۣ۟ۢۢۡ
com/pandora/core/ۣۥۨۤ
com/ss/android/update/ۡ۠ۥۥ
com/ss/android/update/ۣۨ۟
com/tY
```

> 画像独有（番茄有红果无，信息项）: 88 主类

## 8. com/b/a C 类家族存续点位复扫（v7.3.7.32，只读）

> 口径=HG-2 invoke-NOP 同款（com/b/ 本体自引用豁免）。判定权在老马：本节仅列存续事实。

### 家族类清单（3 类；v736 基线 3 类）

| 类 | .method 数 | 含关键链方法 | 特征字符串命中 |
|---|---|---|---|
| `com/b/a` | 5 | init getApplication getID getReflect | ActivityThread×2 deviceid×3 |
| `com/b/a$Android_id` | 2 | - | Settings$Secure×1 android_id×1 |
| `com/b/a$Reflect` | 5 | - | - |

- 基线类缺失（v736 有 v737 无）: 无
- 家族新增成员（v736 无 v737 有）: 无

### 外部 invoke 点位（com/b 之外 → Lcom/b/a;）：1 条 / 1 文件（v736 基线 1 点位）

| 文件 | 所在 .method | 指令 |
|---|---|---|
| `classes14/com/tencent/tinker/loader/MuteApplication.smali` | `.method public onCreate()V` | `invoke-static {}, Lcom/b/a;->init()V` |

### 非 invoke 引用（字段/类型引用等，信息项）：0 条

### 点分字符串形态（"com.b.a"，反射/Class.forName 面，信息项）：0 条

- 家族本体自引用文件数: 2（v736 基线 2，豁免不参与计数）
- **官方内层引用 Lcom/b/a; 的文件数: 0；内层 com/b/ 路径类文件: 0（两者必须=0，非 0=内层官方包本身带链，重大红旗）**

## 9. 外层 dex 归属分析（v7.3.7.32：壳 dex vs 官方 dex）

> 判据：类名对齐（同 §1 口径）。重排堆dex=added≈0 且 official 全为挪位；注入堆dex=added 占比高。判定权在老马。

- 外层 dex: 24 个 ｜ 内层官方 dex: 22 个 ｜ 外层独有 dex 名: `classes23`, `classes24` ｜ 内层独有（壳未带）: 无

| 外层dex | 类总数 | 真新增 | 官方就地¹ | 官方挪位² | 新增占比 |
|---|---|---|---|---|---|
| `classes` | 11618 | 0 | 11618 | 0 | 0.0% |
| `classes2` | 13009 | 0 | 12579 | 430 | 0.0% |
| `classes3` | 14364 | 0 | 13269 | 1095 | 0.0% |
| `classes4` | 13936 | 0 | 12643 | 1293 | 0.0% |
| `classes5` | 16585 | 0 | 14190 | 2395 | 0.0% |
| `classes6` | 16374 | 0 | 12825 | 3549 | 0.0% |
| `classes7` | 12156 | 0 | 7920 | 4236 | 0.0% |
| `classes8` | 11580 | 0 | 6503 | 5077 | 0.0% |
| `classes9` | 10478 | 0 | 6768 | 3710 | 0.0% |
| `classes10` | 13999 | 0 | 6357 | 7642 | 0.0% |
| `classes11` | 10092 | 0 | 3889 | 6203 | 0.0% |
| `classes12` | 11547 | 0 | 5559 | 5988 | 0.0% |
| `classes13` | 10483 | 0 | 2296 | 8187 | 0.0% |
| `classes14` | 9115 | 0 | 2930 | 6185 | 0.0% |
| `classes15` | 12143 | 0 | 2234 | 9909 | 0.0% |
| `classes16` | 11131 | 0 | 7416 | 3715 | 0.0% |
| `classes17` | 10767 | 0 | 7181 | 3586 | 0.0% |
| `classes18` | 11443 | 0 | 7188 | 4255 | 0.0% |
| `classes19` | 12762 | 0 | 6435 | 6327 | 0.0% |
| `classes20` | 11895 | 0 | 5756 | 6139 | 0.0% |
| `classes21` | 13731 | 0 | 5394 | 8337 | 0.0% |
| `classes22` | 14543 | 0 | 5043 | 9500 | 0.0% |
| `classes23` ★ | 14791 | 56 | 0 | 14735 | 0.4% |
| `classes24` ★ | 2102 | 1172 | 0 | 930 | 55.8% |

¹ 官方类在内层同名 dex 出现（就近未动） ｜ ² 官方类来自内层其他 dex（重打包挪位）

### ★ 外层独有 `classes23.dex` 解剖（14791 类）

- 真新增: **56** ｜ 官方挪入: **14735**
- 官方来源分布（前 8）: `classes22`×13849、`classes3`×711、`classes20`×77、`classes21`×55、`classes7`×41、`classes10`×2
- 新增包前缀分布（前 8）: `com/dragon/`×32、`org/lsposed/`×12、`com/b/`×3、`an2/۟ۡۧۤۧ/`×1、`an2/۟ۢۢ۠ۦ/`×1、`an2/۟ۦۧۤ۟/`×1、`an2/۟ۦۨۢۤ/`×1、`an2/ۡۥ۠ۦ/`×1
- 机械判读（建议，非终判）: **重排为主、少量新增**

### ★ 外层独有 `classes24.dex` 解剖（2102 类）

- 真新增: **1172** ｜ 官方挪入: **930**
- 官方来源分布（前 8）: `classes10`×578、`classes7`×262、`classes9`×84、`classes8`×6
- 新增包前缀分布（前 8）: `com/dragon/`×45、`org/checkerframework/`×34、`com/pandora/`×7、`com/ss/`×3、`com/A/`×1、`com/B/`×1、`com/C/`×1、`com/D/`×1
- 机械判读（建议，非终判）: **新增注入堆（重点排查对象）**

- 全树官方类挪位总数（重排规模）: 123423
