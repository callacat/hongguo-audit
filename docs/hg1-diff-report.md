# HG-1 红果外层 dex 全量 diff 报告（外层 23 dex vs 内嵌官方原包 21 dex）

> 方法=类名对齐+调试指令剥离（继承番茄 round16a 两轮修正）。分类权在老马：
> A=壳代码(番茄画像重合) / B=去广告会员patch / C=可疑新增(番茄壳中不存在) / D=VIP伪造保留

## 1. 总览

- 外层类总数: 283855 ｜ 内层官方类总数: 282632
- **真新增类: 1223**（全文见 hg1-diff-baksmali/added/）
- **真删除类: 0**（全文见 hg1-diff-baksmali/removed/）
- **修改类: 3539**（差异方法全文见 hg1-diff-baksmali/changed/，[MOD-ADDED]/[MOD-CHANGED vs INNER-ORIGINAL]/[INNER-REMOVED-IN-MOD] 三段标注）
- 修改类中差异方法: 新增 14021 / 删除 30 / 修改 9921

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
- `com/tZ.smali`
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
- `com/ua.smali`
- `com/v.smali`
- `com/w.smali`
- `com/x.smali`
- `com/y.smali`
- `com/z.smali`

### `com/dragon/` — 61 类
- `com/dragon/read/ad/util/ۣۤۢ۟.smali`
- `com/dragon/read/base/ssconfig/model/۟۠ۢۢ.smali`
- `com/dragon/read/base/ssconfig/model/۟ۤۦۨۧ.smali`
- `com/dragon/read/base/ssconfig/model/۟ۥۡۨۧ.smali`
- `com/dragon/read/base/ssconfig/model/ۣۡۨۥ.smali`
- `com/dragon/read/base/ssconfig/model/ۣۤۢۦ.smali`
- `com/dragon/read/base/ssconfig/model/ۤۧ۠ۦ.smali`
- `com/dragon/read/base/ssconfig/model/ۥۡۢ۠.smali`
- `com/dragon/read/base/ssconfig/model/ۣۣۧۤ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/۟ۤۢۡۥ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/۟ۥۥۣۡ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/۟ۦۢۨۤ.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/ۣۣ۟ۧ۠.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/ۣ۟ۧۦ۟.smali`
- `com/dragon/read/component/biz/impl/mine/card/model/۟ۧۤۢۤ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/۟۠ۥۦ۠.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/۟ۦ۠ۦۥ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/۟ۧۧۥۨ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/۠ۥۥ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۣۡ۟ۥ.smali`
- `com/dragon/read/component/biz/impl/mine/loginv2/view/ۤۦ۠ۡ.smali`
- `com/dragon/read/component/biz/impl/mine/۟۟ۤۦۡ.smali`
- `com/dragon/read/component/biz/impl/mine/۟ۢۥۣۢ.smali`
- `com/dragon/read/component/biz/impl/mine/ۣ۟ۨۢۧ.smali`
- `com/dragon/read/component/biz/impl/mine/۟ۦ۠ۢ۠.smali`
- `com/dragon/read/component/biz/impl/mine/۟ۧۡۨۡ.smali`
- `com/dragon/read/component/biz/impl/mine/ۣۣ.smali`
- `com/dragon/read/pages/main/۟ۥۣۦۢ.smali`
- `com/dragon/read/pages/main/۟ۥۦۧۥ.smali`
- `com/dragon/read/pages/main/ۨۦۡۡ.smali`
- `com/dragon/read/polaris/۟۟۠ۥ.smali`
- `com/dragon/read/polaris/۟۠ۦۨۢ.smali`
- `com/dragon/read/polaris/۟۠ۧ۠۟.smali`
- `com/dragon/read/polaris/۟ۢ۟ۡ۟.smali`
- `com/dragon/read/polaris/ۣۣ۟۠۟.smali`
- `com/dragon/read/polaris/۟ۤ۟۠ۥ.smali`
- `com/dragon/read/polaris/ۣ۠ۨۨ.smali`
- `com/dragon/read/polaris/ۧۢۨ۟.smali`
- `com/dragon/read/reader/ad/noad/۟۠ۥۤۢ.smali`
- `com/dragon/read/reader/ad/noad/ۢۨۧۧ.smali`
- `com/dragon/read/reader/ad/noad/ۤۥۧ۠.smali`
- `com/dragon/read/reader/ad/۟ۦۣۣۣ.smali`
- `com/dragon/read/reader/ad/ۣ۠ۢۨ.smali`
- `com/dragon/read/reader/ad/ۣۡۨۧ.smali`
- `com/dragon/read/reader/ad/ۢۨ۠ۡ.smali`
- `com/dragon/read/reader/ad/ۤۢۢۤ.smali`
- `com/dragon/read/reader/ad/ۤۥۧ.smali`
- `com/dragon/read/reader/ad/ۦۣۧۢ.smali`
- `com/dragon/read/rpc/rpc/ۣۣ۟۟ۤ.smali`
- `com/dragon/read/rpc/rpc/۟ۡۦ۟ۥ.smali`
- `com/dragon/read/rpc/rpc/ۣ۟ۧ۟ۡ.smali`
- `com/dragon/read/rpc/rpc/۟ۧۦۡۥ.smali`
- `com/dragon/read/rpc/rpc/ۡ۠ۤۧ.smali`
- `com/dragon/read/rpc/rpc/ۣ۠ۤۦ.smali`
- `com/dragon/read/rpc/rpc/ۨۦۤ.smali`
- `com/dragon/read/user/model/۟ۤۧۢ.smali`
- `com/dragon/read/user/model/۟ۥ۟ۦ.smali`
- `com/dragon/read/user/model/۟ۦۣۢۡ.smali`
- `com/dragon/read/user/model/۟ۧۦۣ.smali`
- `com/dragon/read/user/model/ۦۣۣۧ.smali`
- `com/dragon/read/util/ۦۧۥۡ.smali`

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

### `com/pandora/` — 12 类
- `com/pandora/core/AppFactory$DATA.smali`
- `com/pandora/core/AppFactory.smali`
- `com/pandora/core/Copyright.smali`
- `com/pandora/core/CreatorProxy.smali`
- `com/pandora/core/۟ۡۥۨ.smali`
- `com/pandora/core/۟ۢۡ۠ۤ.smali`
- `com/pandora/core/ۣ۟ۦ.smali`
- `com/pandora/core/۟ۤ۠ۨ۠.smali`
- `com/pandora/core/۟ۤۧۢۥ.smali`
- `com/pandora/core/۟ۧۥۦۣ.smali`
- `com/pandora/core/ۡۢۦۤ.smali`
- `com/pandora/core/ۢۧ۠ۥ.smali`

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

### `com/ss/` — 10 类
- `com/ss/android/update/۟۟ۤۤۡ.smali`
- `com/ss/android/update/ۣۣ۟ۢۨ.smali`
- `com/ss/android/update/۟ۤۡۡۤ.smali`
- `com/ss/android/update/۟ۤۤۨۥ.smali`
- `com/ss/android/update/۟ۥۧۦۣ.smali`
- `com/ss/android/update/ۣۥۣۣ.smali`
- `com/ss/android/update/ۣۣۨۨ.smali`
- `com/ss/android/update/ۦۥ۠ۡ.smali`
- `com/ss/android/update/ۧ۠ۧۨ.smali`
- `com/ss/android/update/ۣۧ۟ۥ.smali`

### `an2/` — 7 类
- `an2/۟۠ۢۥ.smali`
- `an2/ۣ۟ۧۢۤ.smali`
- `an2/۠ۤۦۣ.smali`
- `an2/ۡۨۡۥ.smali`
- `an2/ۣۣۥ۟.smali`
- `an2/ۣۤۡۧ.smali`
- `an2/ۧۨ۟۟.smali`

### `com/b/` — 3 类
- `com/b/a$Android_id.smali`
- `com/b/a$Reflect.smali`
- `com/b/a.smali`

### `sgcore0/` — 1 类
- `sgcore0/SafeLoader.smali`

### `sgcore0/hidden/` — 1 类
- `sgcore0/hidden/Hidden0.smali`

## 3. 修改类清单（按差异方法总数降序）

| 类 | +新增 | -删除 | ~修改 | 合计 |
|---|---|---|---|---|
| `com/dragon/read/pages/main/MainFragmentActivity.smali` | 1033 | 0 | 130 | 1163 |
| `com/dragon/read/util/DebugManager.smali` | 70 | 0 | 509 | 579 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2.smali` | 414 | 0 | 63 | 477 |
| `com/dragon/read/rpc/rpc/UgcApiService.smali` | 203 | 0 | 203 | 406 |
| `com/dragon/read/rpc/rpc/UserApiService.smali` | 179 | 0 | 179 | 358 |
| `com/dragon/read/reader/ad/ReaderAdManager.smali` | 299 | 0 | 35 | 334 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment.smali` | 189 | 0 | 40 | 229 |
| `com/dragon/read/pages/main/j2.smali` | 212 | 0 | 2 | 214 |
| `com/dragon/read/util/ImageLoaderUtils.smali` | 111 | 0 | 72 | 183 |
| `com/dragon/read/util/l4.smali` | 159 | 0 | 12 | 171 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment.smali` | 146 | 0 | 14 | 160 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2.smali` | 139 | 0 | 18 | 157 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment.smali` | 116 | 0 | 37 | 153 |
| `com/dragon/read/util/j.smali` | 116 | 0 | 27 | 143 |
| `com/dragon/read/util/ApkSizeOptImageLoader.smali` | 131 | 0 | 9 | 140 |
| `com/dragon/read/util/BookUtils.smali` | 56 | 0 | 77 | 133 |
| `com/ss/android/update/z.smali` | 66 | 24 | 42 | 132 |
| `com/dragon/read/ad/util/AdUtil.smali` | 113 | 0 | 10 | 123 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment.smali` | 88 | 0 | 28 | 116 |
| `com/dragon/read/pages/main/MainFragmentActivity$b0.smali` | 113 | 0 | 2 | 115 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard.smali` | 93 | 0 | 15 | 108 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment.smali` | 91 | 0 | 13 | 104 |
| `com/dragon/read/util/r8.smali` | 91 | 0 | 8 | 99 |
| `an2/d.smali` | 81 | 0 | 13 | 94 |
| `com/dragon/read/pages/main/j4.smali` | 71 | 1 | 21 | 93 |
| `com/ss/videoarch/liveplayer/VideoLiveManager.smali` | 0 | 0 | 91 | 91 |
| `com/dragon/read/util/ToastUtils.smali` | 35 | 0 | 54 | 89 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment.smali` | 63 | 0 | 24 | 87 |
| `com/dragon/read/util/PictureUtils.smali` | 48 | 0 | 34 | 82 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity.smali` | 68 | 0 | 13 | 81 |
| `com/dragon/read/pages/main/v2.smali` | 70 | 0 | 5 | 75 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineConfigImpl.smali` | 48 | 0 | 19 | 67 |
| `com/dragon/read/pages/main/MainPageDrawerLayout.smali` | 7 | 0 | 59 | 66 |
| `com/ss/android/update/UpdateServiceImpl.smali` | 10 | 0 | 56 | 66 |
| `com/dragon/read/ad/util/t0.smali` | 42 | 0 | 22 | 64 |
| `com/dragon/read/util/BitmapUtils.smali` | 21 | 0 | 42 | 63 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil.smali` | 54 | 0 | 7 | 61 |
| `com/dragon/read/pages/main/m.smali` | 57 | 0 | 4 | 61 |
| `com/dragon/read/ad/util/b0.smali` | 53 | 0 | 7 | 60 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment.smali` | 34 | 0 | 24 | 58 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity.smali` | 48 | 0 | 10 | 58 |
| `com/dragon/read/util/l2.smali` | 48 | 0 | 9 | 57 |
| `com/dragon/read/reader/ad/AdLine.smali` | 42 | 0 | 14 | 56 |
| `com/dragon/read/util/AbiUtil.smali` | 34 | 0 | 22 | 56 |
| `com/dragon/read/util/CdnLargeImageLoader.smali` | 40 | 0 | 16 | 56 |
| `com/dragon/read/util/j1.smali` | 24 | 0 | 32 | 56 |
| `com/dragon/read/component/biz/impl/mine/NewAboutActivity.smali` | 45 | 0 | 10 | 55 |
| `com/dragon/read/component/biz/impl/mine/i9.smali` | 52 | 0 | 2 | 54 |
| `com/dragon/read/util/UiUtils.smali` | 6 | 0 | 48 | 54 |
| `com/dragon/read/util/t0.smali` | 43 | 0 | 11 | 54 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtilsInner.smali` | 0 | 0 | 52 | 52 |
| `com/dragon/read/ad/util/z0.smali` | 42 | 0 | 9 | 51 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberNormalView.smali` | 36 | 0 | 15 | 51 |
| `com/dragon/read/pages/main/MainFragmentActivity$q.smali` | 49 | 0 | 2 | 51 |
| `com/dragon/read/util/RecentConsumeRecorder.smali` | 42 | 0 | 9 | 51 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberNormalViewForFullScreenVideo.smali` | 35 | 0 | 15 | 50 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/b.smali` | 43 | 0 | 7 | 50 |
| `com/dragon/read/pages/main/z.smali` | 40 | 0 | 10 | 50 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$g.smali` | 46 | 0 | 3 | 49 |
| `com/dragon/read/reader/ad/ReaderAdManager$a.smali` | 47 | 0 | 2 | 49 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity.smali` | 34 | 0 | 13 | 47 |
| `com/dragon/read/util/UiConfigSetter.smali` | 18 | 0 | 29 | 47 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/a.smali` | 39 | 0 | 7 | 46 |
| `com/dragon/read/util/FileUtils.smali` | 13 | 0 | 33 | 46 |
| `com/ss/videoarch/liveplayer/log/LiveLoggerService.smali` | 0 | 0 | 46 | 46 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$c.smali` | 32 | 0 | 12 | 44 |
| `com/dragon/read/util/h.smali` | 40 | 0 | 4 | 44 |
| `com/dragon/read/util/k.smali` | 32 | 0 | 12 | 44 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$b.smali` | 37 | 0 | 5 | 42 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2$a.smali` | 40 | 0 | 2 | 42 |
| `com/dragon/read/component/biz/impl/mine/l7.smali` | 40 | 0 | 2 | 42 |
| `com/dragon/read/util/r8$b.smali` | 37 | 0 | 5 | 42 |
| `com/dragon/read/ad/util/h0.smali` | 36 | 0 | 5 | 41 |
| `com/dragon/read/util/UriUtils.smali` | 19 | 0 | 22 | 41 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/d.smali` | 32 | 0 | 8 | 40 |
| `com/dragon/read/pages/main/e5.smali` | 33 | 0 | 7 | 40 |
| `com/dragon/read/rpc/rpc/MsgApiService.smali` | 20 | 0 | 20 | 40 |
| `com/dragon/read/util/v.smali` | 36 | 0 | 4 | 40 |
| `an2/f.smali` | 28 | 0 | 11 | 39 |
| `com/dragon/read/pages/main/q4.smali` | 28 | 0 | 11 | 39 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$Companion.smali` | 35 | 0 | 4 | 39 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog.smali` | 32 | 0 | 7 | 39 |
| `com/dragon/read/util/ReaderCommonColor.smali` | 8 | 0 | 31 | 39 |
| `com/dragon/read/component/biz/impl/mine/DiggContentActivity.smali` | 30 | 0 | 8 | 38 |
| `com/dragon/read/pages/main/g.smali` | 29 | 0 | 9 | 38 |
| `com/dragon/read/reader/ad/a0.smali` | 28 | 1 | 8 | 37 |
| `com/dragon/read/reader/ad/h.smali` | 11 | 0 | 26 | 37 |
| `com/dragon/read/util/NetReqUtil.smali` | 25 | 0 | 12 | 37 |
| `com/dragon/read/util/f5.smali` | 27 | 0 | 10 | 37 |
| `com/dragon/read/user/model/PrivilegeInfoModel.smali` | 15 | 0 | 21 | 36 |
| `com/dragon/read/util/PremiumReportHelper.smali` | 18 | 0 | 18 | 36 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenLoginActivity.smali` | 20 | 0 | 15 | 35 |
| `com/dragon/read/pages/main/s4.smali` | 31 | 0 | 4 | 35 |
| `com/dragon/read/util/d4.smali` | 30 | 0 | 5 | 35 |
| `an2/g.smali` | 5 | 0 | 29 | 34 |
| `com/dragon/read/ad/util/j0.smali` | 20 | 0 | 14 | 34 |
| `com/dragon/read/component/biz/impl/mine/LoginActivity.smali` | 24 | 0 | 10 | 34 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment.smali` | 14 | 0 | 20 | 34 |
| `com/dragon/read/component/biz/impl/mine/de.smali` | 32 | 0 | 2 | 34 |
| `com/dragon/read/pages/main/q.smali` | 32 | 0 | 2 | 34 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$a.smali` | 31 | 0 | 2 | 33 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/l.smali` | 29 | 0 | 4 | 33 |
| `com/dragon/read/component/biz/impl/mine/dc.smali` | 20 | 0 | 12 | 32 |
| `com/dragon/read/pages/main/IFixRefreshBottomTab$$Impl.smali` | 28 | 0 | 4 | 32 |
| `com/dragon/read/reader/ad/d.smali` | 24 | 0 | 8 | 32 |
| `an2/b.smali` | 29 | 0 | 2 | 31 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/f.smali` | 23 | 0 | 8 | 31 |
| `com/dragon/read/util/d8.smali` | 6 | 0 | 25 | 31 |
| `com/dragon/read/util/i5.smali` | 24 | 0 | 7 | 31 |
| `com/dragon/read/util/m4.smali` | 25 | 0 | 6 | 31 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/j.smali` | 26 | 0 | 4 | 30 |
| `com/dragon/read/pages/main/MainFragmentActivity$d0.smali` | 27 | 0 | 3 | 30 |
| `com/dragon/read/reader/ad/c.smali` | 26 | 0 | 4 | 30 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/g.smali` | 0 | 0 | 29 | 29 |
| `com/dragon/read/ad/util/p0.smali` | 22 | 0 | 7 | 29 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenBindDouyinActivity.smali` | 17 | 0 | 12 | 29 |
| `com/dragon/read/pages/main/k.smali` | 25 | 0 | 4 | 29 |
| `com/dragon/read/util/p0.smali` | 26 | 0 | 2 | 28 |
| `com/ss/android/update/UpdateProgressActivity.smali` | 10 | 0 | 18 | 28 |
| `com/dragon/read/component/biz/impl/mine/pg.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/component/biz/impl/mine/ra.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/pages/main/PermissionGuidanceDialogActivity.smali` | 18 | 0 | 9 | 27 |
| `com/dragon/read/pages/main/e.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/util/i0.smali` | 25 | 0 | 2 | 27 |
| `com/dragon/read/util/l3.smali` | 25 | 0 | 2 | 27 |
| `an2/c.smali` | 22 | 0 | 4 | 26 |
| `com/dragon/read/ad/util/e.smali` | 20 | 0 | 6 | 26 |
| `com/dragon/read/ad/util/i.smali` | 24 | 0 | 2 | 26 |
| `com/dragon/read/component/biz/impl/mine/vc.smali` | 21 | 0 | 5 | 26 |
| `com/dragon/read/pages/main/MainFragmentActivity$r.smali` | 24 | 0 | 2 | 26 |
| `com/dragon/read/pages/main/l.smali` | 24 | 0 | 2 | 26 |
| `com/dragon/read/util/CustomFrescoMonitor.smali` | 19 | 0 | 7 | 26 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$h.smali` | 23 | 0 | 2 | 25 |
| `com/dragon/read/component/biz/impl/mine/f7.smali` | 15 | 0 | 10 | 25 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$h.smali` | 21 | 0 | 3 | 24 |
| `com/dragon/read/util/z7.smali` | 19 | 0 | 5 | 24 |
| `com/ss/android/update/z$b.smali` | 22 | 0 | 2 | 24 |
| `com/dragon/read/component/biz/impl/mine/BsMineFragmentFactory.smali` | 14 | 0 | 9 | 23 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$b.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/component/biz/impl/mine/se.smali` | 18 | 0 | 5 | 23 |
| `com/dragon/read/pages/main/o4.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/pages/main/p.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/pages/main/w.smali` | 21 | 0 | 2 | 23 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$a.smali` | 20 | 0 | 3 | 23 |
| `com/dragon/read/util/MeasureUtil.smali` | 9 | 0 | 14 | 23 |
| `com/dragon/read/util/PictureUtils$g.smali` | 20 | 0 | 3 | 23 |
| `com/dragon/read/util/w6.smali` | 19 | 0 | 4 | 23 |
| `com/ss/android/update/x.smali` | 5 | 0 | 18 | 23 |
| `an2/a.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/component/biz/impl/mine/a8.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/component/biz/impl/mine/eg.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/k.smali` | 18 | 0 | 4 | 22 |
| `com/dragon/read/util/NumberUtils.smali` | 3 | 0 | 19 | 22 |
| `com/dragon/read/util/b3.smali` | 18 | 0 | 4 | 22 |
| `com/dragon/read/util/i7.smali` | 10 | 0 | 12 | 22 |
| `com/dragon/read/util/r0.smali` | 20 | 0 | 2 | 22 |
| `com/dragon/read/ad/util/q.smali` | 17 | 0 | 4 | 21 |
| `com/dragon/read/ad/util/r0.smali` | 18 | 0 | 3 | 21 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$e.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/component/biz/impl/mine/RapidLoginFragment.smali` | 14 | 0 | 7 | 21 |
| `com/dragon/read/component/biz/impl/mine/l9.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/pages/main/n0.smali` | 18 | 0 | 3 | 21 |
| `com/dragon/read/pages/main/z$f.smali` | 19 | 0 | 2 | 21 |
| `com/dragon/read/util/f2.smali` | 1 | 0 | 20 | 21 |
| `com/dragon/read/util/m1.smali` | 12 | 0 | 9 | 21 |
| `com/dragon/read/ad/util/d.smali` | 12 | 0 | 8 | 20 |
| `com/dragon/read/component/biz/impl/mine/c.smali` | 13 | 0 | 7 | 20 |
| `com/dragon/read/component/biz/impl/mine/mb.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/component/biz/impl/mine/mf.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/pages/main/i3.smali` | 7 | 0 | 13 | 20 |
| `com/dragon/read/pages/main/j.smali` | 2 | 0 | 18 | 20 |
| `com/dragon/read/util/h5.smali` | 18 | 0 | 2 | 20 |
| `com/dragon/read/util/k4.smali` | 16 | 0 | 4 | 20 |
| `com/dragon/read/util/kb.smali` | 14 | 0 | 6 | 20 |
| `com/dragon/read/util/q6.smali` | 15 | 0 | 5 | 20 |
| `com/dragon/read/ad/util/f.smali` | 15 | 0 | 4 | 19 |
| `com/dragon/read/component/biz/impl/mine/ta.smali` | 17 | 0 | 2 | 19 |
| `com/dragon/read/pages/main/a4.smali` | 14 | 0 | 5 | 19 |
| `com/dragon/read/pages/main/f4.smali` | 15 | 0 | 4 | 19 |
| `com/dragon/read/pages/main/w1.smali` | 17 | 0 | 2 | 19 |
| `com/dragon/read/reader/ad/OfflineDefaultAdLine.smali` | 12 | 0 | 7 | 19 |
| `com/dragon/read/reader/ad/ReaderAdManager$f.smali` | 17 | 0 | 2 | 19 |
| `com/dragon/read/util/sa.smali` | 13 | 0 | 6 | 19 |
| `com/dragon/read/ad/util/f1.smali` | 15 | 0 | 3 | 18 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentProvider.smali` | 10 | 0 | 8 | 18 |
| `com/dragon/read/component/biz/impl/mine/l.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/component/biz/impl/mine/vg.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/util/a2.smali` | 10 | 0 | 8 | 18 |
| `com/dragon/read/util/f6.smali` | 11 | 0 | 7 | 18 |
| `com/dragon/read/util/m5.smali` | 12 | 0 | 6 | 18 |
| `com/dragon/read/util/p4.smali` | 15 | 0 | 3 | 18 |
| `com/dragon/read/util/p6.smali` | 16 | 0 | 2 | 18 |
| `com/dragon/read/util/r.smali` | 4 | 0 | 14 | 18 |
| `com/dragon/read/util/t7.smali` | 13 | 0 | 5 | 18 |
| `com/ss/android/update/v.smali` | 6 | 0 | 12 | 18 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$g.smali` | 11 | 0 | 6 | 17 |
| `com/dragon/read/component/biz/impl/mine/pe.smali` | 15 | 0 | 2 | 17 |
| `com/dragon/read/pages/main/MainFragmentActivity$a0.smali` | 16 | 0 | 1 | 17 |
| `com/dragon/read/pages/main/d3.smali` | 15 | 0 | 2 | 17 |
| `com/dragon/read/pages/main/g3.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/pages/main/q3.smali` | 13 | 0 | 4 | 17 |
| `com/dragon/read/pages/main/x0.smali` | 15 | 0 | 2 | 17 |
| `com/dragon/read/polaris/PolarisConfigCenter.smali` | 10 | 0 | 7 | 17 |
| `com/dragon/read/util/a0.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/util/cb.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/util/fb.smali` | 14 | 0 | 3 | 17 |
| `com/dragon/read/ad/util/g0.smali` | 13 | 0 | 3 | 16 |
| `com/dragon/read/ad/util/h.smali` | 10 | 0 | 6 | 16 |
| `com/dragon/read/ad/util/i0.smali` | 11 | 0 | 5 | 16 |
| `com/dragon/read/component/biz/impl/mine/HongguoEntryActivity.smali` | 8 | 0 | 8 | 16 |
| `com/dragon/read/component/biz/impl/mine/ng.smali` | 12 | 0 | 4 | 16 |
| `com/dragon/read/component/biz/impl/mine/oe.smali` | 14 | 0 | 2 | 16 |
| `com/dragon/read/pages/main/i.smali` | 9 | 0 | 7 | 16 |
| `com/dragon/read/pages/main/w3.smali` | 14 | 0 | 2 | 16 |
| `com/dragon/read/util/ImageViewExtKt.smali` | 7 | 0 | 9 | 16 |
| `com/dragon/read/util/m0.smali` | 12 | 0 | 4 | 16 |
| `com/dragon/read/util/v4.smali` | 12 | 0 | 4 | 16 |
| `com/dragon/read/util/x5.smali` | 14 | 0 | 2 | 16 |
| `com/ss/android/update/i.smali` | 8 | 0 | 8 | 16 |
| `com/ss/android/update/u.smali` | 7 | 0 | 9 | 16 |
| `com/ss/videoarch/liveplayer/model/LiveStreamInfo.smali` | 0 | 0 | 16 | 16 |
| `com/dragon/read/ad/util/b1.smali` | 12 | 0 | 3 | 15 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$onCreate$1$2$1$2$1.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/HalfScreenBindDouyinFragment.smali` | 12 | 0 | 3 | 15 |
| `com/dragon/read/component/biz/impl/mine/HongguoKmpWatchPreferenceFragment$b.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment$a.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$initHonorListView$1.smali` | 11 | 0 | 4 | 15 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$o.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/e8.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/n7.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/og.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/component/biz/impl/mine/wg.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/a4$b.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/d0.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/p1.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/pages/main/z$e.smali` | 14 | 0 | 1 | 15 |
| `com/dragon/read/reader/ad/FrontAdLine.smali` | 10 | 0 | 5 | 15 |
| `com/dragon/read/reader/ad/k.smali` | 10 | 0 | 5 | 15 |
| `com/dragon/read/reader/ad/v.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/util/AudioUtil.smali` | 9 | 0 | 6 | 15 |
| `com/dragon/read/util/ImageLoaderUtils$a.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/util/b8.smali` | 7 | 0 | 8 | 15 |
| `com/dragon/read/util/g0.smali` | 8 | 0 | 7 | 15 |
| `com/dragon/read/util/g6.smali` | 13 | 0 | 2 | 15 |
| `com/dragon/read/util/s5.smali` | 9 | 0 | 6 | 15 |
| `com/dragon/read/util/t.smali` | 10 | 0 | 5 | 15 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/c0.smali` | 0 | 0 | 14 | 14 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0.smali` | 0 | 0 | 14 | 14 |
| `com/dragon/read/ad/util/y.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$d.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity$b.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/ef.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/hg.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/CaptchaViewV2.smali` | 6 | 0 | 8 | 14 |
| `com/dragon/read/component/biz/impl/mine/p9.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/r8.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/sf.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/component/biz/impl/mine/xe.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/a.smali` | 9 | 0 | 5 | 14 |
| `com/dragon/read/pages/main/d5.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/h2.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/z$a.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/pages/main/z$g.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/reader/ad/x.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/CdnImageCacheEventListener.smali` | 6 | 0 | 8 | 14 |
| `com/dragon/read/util/CommonUiFlow.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/util/ExtractColorHost.smali` | 9 | 0 | 5 | 14 |
| `com/dragon/read/util/ImageLoaderUtils$a$a.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/StringUtils.smali` | 2 | 0 | 12 | 14 |
| `com/dragon/read/util/UiConfigSetter$adjust$1.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/util/a1.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/b7.smali` | 6 | 0 | 8 | 14 |
| `com/dragon/read/util/c1.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/f.smali` | 10 | 0 | 4 | 14 |
| `com/dragon/read/util/k3.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/l1.smali` | 8 | 0 | 6 | 14 |
| `com/dragon/read/util/m3.smali` | 12 | 0 | 2 | 14 |
| `com/dragon/read/util/r$a.smali` | 2 | 0 | 12 | 14 |
| `com/dragon/read/util/u6.smali` | 7 | 0 | 7 | 14 |
| `com/dragon/read/util/va.smali` | 11 | 0 | 3 | 14 |
| `com/dragon/read/util/y3$a.smali` | 12 | 0 | 2 | 14 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper.smali` | 0 | 0 | 13 | 13 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$c.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/b0$a.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/b0$b.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/b0$c.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/ad/util/b0$d.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$f.smali` | 9 | 0 | 4 | 13 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$e.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/cb.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/lf.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/ne.smali` | 6 | 0 | 7 | 13 |
| `com/dragon/read/component/biz/impl/mine/qf.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/s7.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/t8.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/component/biz/impl/mine/v7.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/MainFragmentActivity$s.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/MiraCastMonitor.smali` | 9 | 0 | 4 | 13 |
| `com/dragon/read/pages/main/g0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/h0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/h3.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/pages/main/k1.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/pages/main/u2.smali` | 5 | 0 | 8 | 13 |
| `com/dragon/read/util/CoroutineExecutor$execute$1.smali` | 9 | 0 | 4 | 13 |
| `com/dragon/read/util/FrequencyMgr.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/util/ImageLoaderUtils$u$a.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/util/c2.smali` | 6 | 0 | 7 | 13 |
| `com/dragon/read/util/d0.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/util/e3.smali` | 10 | 0 | 3 | 13 |
| `com/dragon/read/util/f7.smali` | 8 | 0 | 5 | 13 |
| `com/dragon/read/util/g1.smali` | 6 | 0 | 7 | 13 |
| `com/dragon/read/util/h0.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/util/i.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/util/r2.smali` | 11 | 0 | 2 | 13 |
| `com/dragon/read/util/z3.smali` | 10 | 0 | 3 | 13 |
| `com/ss/android/update/q.smali` | 6 | 0 | 7 | 13 |
| `zb/b.smali` | 0 | 0 | 13 | 13 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/utils/PreVerifyEventUtils.smali` | 0 | 0 | 12 | 12 |
| `com/android/ttcjpaysdk/verify/utils/j.smali` | 0 | 0 | 12 | 12 |
| `com/dragon/read/ad/util/m.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$b.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/HongguoKmpWatchPreferenceFragment$a.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/HongguoKmpWatchPreferenceFragment.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$q.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$o.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$e.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$a.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$i.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/ProfileItemChangeActivity$c.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$a.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$c.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/ac.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/af.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/d.smali` | 5 | 0 | 7 | 12 |
| `com/dragon/read/component/biz/impl/mine/ge.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/hf.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/kb.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/kf.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c.smali` | 5 | 0 | 7 | 12 |
| `com/dragon/read/component/biz/impl/mine/m.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/na.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/component/biz/impl/mine/rf.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/sa.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/tf.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/ua.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/ue.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/component/biz/impl/mine/va.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/MainFragmentActivity$f.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/l4.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/y4.smali` | 10 | 0 | 2 | 12 |
| `com/dragon/read/pages/main/z3.smali` | 10 | 0 | 2 | 12 |
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
| `com/dragon/read/util/h4.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/util/kb$a.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/util/l0.smali` | 7 | 0 | 5 | 12 |
| `com/dragon/read/util/l7.smali` | 9 | 0 | 3 | 12 |
| `com/dragon/read/util/y7.smali` | 5 | 0 | 7 | 12 |
| `com/dragon/read/util/z4.smali` | 6 | 0 | 6 | 12 |
| `com/ss/videoarch/liveplayer/lss/LSSStrategyController.smali` | 0 | 0 | 12 | 12 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayHomePageMethodModule.smali` | 0 | 0 | 11 | 11 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFragment.smali` | 0 | 0 | 11 | 11 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$a.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$h.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$l.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineTabUIConfig.smali` | 3 | 0 | 8 | 11 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$k.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/e.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/f9.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/ff.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/if.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/LoginTypeView$a.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/LoginTypeView.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/component/biz/impl/mine/tg.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/ud.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/component/biz/impl/mine/vc$a.smali` | 8 | 0 | 3 | 11 |
| `com/dragon/read/pages/main/c5.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/e2.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/l2.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/pages/main/v.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/pages/main/x1.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/user/model/NetIdLoginResp.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/ImageLoaderUtils$r.smali` | 8 | 0 | 3 | 11 |
| `com/dragon/read/util/OOMScoreAdjUtil.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/UiConfigSetter$b.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/UiConfigSetter$k.smali` | 4 | 0 | 7 | 11 |
| `com/dragon/read/util/d5.smali` | 8 | 0 | 3 | 11 |
| `com/dragon/read/util/d6.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/d7.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/e1.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/f1.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/g5.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/h$a.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/h8.smali` | 4 | 0 | 7 | 11 |
| `com/dragon/read/util/n2.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/p1.smali` | 9 | 0 | 2 | 11 |
| `com/dragon/read/util/u7.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/w4.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/x0.smali` | 7 | 0 | 4 | 11 |
| `com/dragon/read/util/x1.smali` | 5 | 0 | 6 | 11 |
| `com/dragon/read/util/y0.smali` | 6 | 0 | 5 | 11 |
| `com/ss/android/update/t.smali` | 5 | 0 | 6 | 11 |
| `com/tencent/mm/opensdk/openapi/BaseWXApiImplV10.smali` | 0 | 0 | 11 | 11 |
| `f9/c.smali` | 0 | 0 | 11 | 11 |
| `com/bytedance/alliance/utils/g.smali` | 0 | 0 | 10 | 10 |
| `com/dragon/read/ad/util/w0.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/ad/util/z.smali` | 7 | 0 | 3 | 10 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$f.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$c.smali` | 9 | 0 | 1 | 10 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$k.smali` | 5 | 0 | 5 | 10 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$l.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$p.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$m.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragmentV2$c.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/be.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/d9.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/e9.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/j8.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/kd.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/kg.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/nf.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/o7.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/of.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/qg.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/wd.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/xb.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/component/biz/impl/mine/ya.smali` | 7 | 0 | 3 | 10 |
| `com/dragon/read/pages/main/c1.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/pages/main/o0.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/pages/main/w2$a.smali` | 9 | 0 | 1 | 10 |
| `com/dragon/read/reader/ad/r.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/CdnLargeImageLoader$a.smali` | 6 | 0 | 4 | 10 |
| `com/dragon/read/util/ColorUtils.smali` | 4 | 0 | 6 | 10 |
| `com/dragon/read/util/NetworkUtils.smali` | 4 | 0 | 6 | 10 |
| `com/dragon/read/util/RecentConsumeRecorder$RecentConsumeParams.smali` | 3 | 0 | 7 | 10 |
| `com/dragon/read/util/RecentConsumeRecorder$RecentSearchParams.smali` | 3 | 0 | 7 | 10 |
| `com/dragon/read/util/UiConfigSetter$f.smali` | 3 | 0 | 7 | 10 |
| `com/dragon/read/util/k1.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/m8.smali` | 4 | 0 | 6 | 10 |
| `com/dragon/read/util/q8.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/s8.smali` | 8 | 0 | 2 | 10 |
| `com/dragon/read/util/y$a.smali` | 6 | 0 | 4 | 10 |
| `com/dragon/read/util/y8.smali` | 7 | 0 | 3 | 10 |
| `com/ss/android/update/z$f.smali` | 7 | 0 | 3 | 10 |
| `com/tencent/tinker/lib/stub/BaseStubContentProvider.smali` | 0 | 0 | 10 | 10 |
| `u9/a.smali` | 0 | 0 | 10 | 10 |
| `com/bytedance/ies/sdk/widgets/priority/GroupSchedule.smali` | 0 | 0 | 9 | 9 |
| `com/dragon/read/ad/util/a.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/ad/util/n0.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/ad/util/p.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/ad/util/u0.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/ad/util/x.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/DataBinderMapperImpl.smali` | 2 | 0 | 7 | 9 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$i.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$i.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/LuckycatLoginFragment$n.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$h.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/ad.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/ca.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/da.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/f7$b.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/component/biz/impl/mine/g8.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/id.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/jd.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/k9.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/ld.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/lg.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/PhoneNumberOneKeyView.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/component/biz/impl/mine/mg.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/nb.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/component/biz/impl/mine/xc.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/MainFragmentActivity$g0.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/pages/main/MiraCastMonitor$b.smali` | 5 | 0 | 4 | 9 |
| `com/dragon/read/pages/main/e0.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/g2.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/o1.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/pages/main/r1.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/reader/ad/l.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/ApkSizeOptImageLoader$a.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/FrequencyMgr$Period$Day.smali` | 5 | 0 | 4 | 9 |
| `com/dragon/read/util/ImageLoaderUtils$o.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/KeyBoardHelper.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/PictureUtils$e.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/PictureUtils$f.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/RxUtils.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/a7$a.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/a8.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/a9.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/c0.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/e4.smali` | 5 | 0 | 4 | 9 |
| `com/dragon/read/util/ea.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/f6$a.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/k$b.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/k$c.smali` | 3 | 0 | 6 | 9 |
| `com/dragon/read/util/l5.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/m6.smali` | 4 | 0 | 5 | 9 |
| `com/dragon/read/util/m7.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/n9.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/o9.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/p5.smali` | 7 | 0 | 2 | 9 |
| `com/dragon/read/util/s.smali` | 6 | 0 | 3 | 9 |
| `com/dragon/read/util/y.smali` | 3 | 0 | 6 | 9 |
| `com/ss/android/update/SSUpdateChecker.smali` | 2 | 0 | 7 | 9 |
| `com/ss/android/update/g0.smali` | 5 | 0 | 4 | 9 |
| `com/ss/android/update/k0.smali` | 5 | 0 | 4 | 9 |
| `com/ss/videoarch/liveplayer/PreloadHelper.smali` | 0 | 0 | 9 | 9 |
| `w50/b.smali` | 0 | 0 | 9 | 9 |
| `yy2/u.smali` | 0 | 0 | 9 | 9 |
| `com/android/ttcjpaysdk/thirdparty/counter/result/fragment/CJPayCompleteFragment.smali` | 0 | 0 | 8 | 8 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyPasswordVM.smali` | 0 | 0 | 8 | 8 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager.smali` | 0 | 0 | 8 | 8 |
| `com/android/ttcjpaysdk/ttcjpayapi/TTCJPayUtils.smali` | 0 | 0 | 8 | 8 |
| `com/bytedance/apm/ApmAgent.smali` | 0 | 0 | 8 | 8 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/b.smali` | 3 | 0 | 5 | 8 |
| `com/dragon/read/ad/util/k.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/k0.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/m0.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/ad/util/o0.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/s.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/t.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/u.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/v.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/ad/util/x0.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/ad/util/y0.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/BindExcludeHongguoServiceImpl.smali` | 3 | 0 | 5 | 8 |
| `com/dragon/read/component/biz/impl/mine/BindToutiaoServiceImpl.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$initHonorListView$1$a.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$b.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/component/biz/impl/mine/LoginFragment$h.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$f.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$e.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$f.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/NewHalfLoginFragment$n.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/b.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/component/biz/impl/mine/ba.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/component/biz/impl/mine/eb.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/h7.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/SingleCodeViewV2.smali` | 3 | 0 | 5 | 8 |
| `com/dragon/read/component/biz/impl/mine/ma.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/nd.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/ne$a.smali` | 4 | 2 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/o9.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/qb.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/s8.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/vd.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/component/biz/impl/mine/z6.smali` | 4 | 0 | 4 | 8 |
| `com/dragon/read/pages/main/MainFragmentActivity$c.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/MainFragmentActivity$x.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/b4.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/l1.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/m$a.smali` | 7 | 0 | 1 | 8 |
| `com/dragon/read/pages/main/n.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/n1.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/o2.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/pages/main/x2$a.smali` | 6 | 0 | 2 | 8 |
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
| `com/dragon/read/util/a3.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/b0.smali` | 1 | 0 | 7 | 8 |
| `com/dragon/read/util/cb$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/f0$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/k5.smali` | 2 | 0 | 6 | 8 |
| `com/dragon/read/util/l6.smali` | 3 | 0 | 5 | 8 |
| `com/dragon/read/util/n1.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/n8.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/na.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/pa.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/q0.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/qa.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/r4.smali` | 3 | 2 | 3 | 8 |
| `com/dragon/read/util/u2.smali` | 6 | 0 | 2 | 8 |
| `com/dragon/read/util/u9.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/v$a.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/y3.smali` | 5 | 0 | 3 | 8 |
| `com/dragon/read/util/za.smali` | 6 | 0 | 2 | 8 |
| `com/ss/android/update/h.smali` | 2 | 0 | 6 | 8 |
| `com/ss/android/update/t$b.smali` | 6 | 0 | 2 | 8 |
| `com/ss/android/update/z$e.smali` | 6 | 0 | 2 | 8 |
| `a02/i.smali` | 0 | 0 | 7 | 7 |
| `a22/b.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/UnifyPreVerifyFingerprintBaseVm.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJPayStandardResultProcess.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/u.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyOneStepPaymentVM.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/n1$b.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/n1.smali` | 0 | 0 | 7 | 7 |
| `com/bytedance/alliance/settings/AllianceLocalSetting$$SettingImpl.smali` | 0 | 0 | 7 | 7 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceProxy.smali` | 0 | 0 | 7 | 7 |
| `com/dragon/read/ad/util/a1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/ad/util/g.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/ad/util/q0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/ad/util/s0.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/component/biz/impl/mine/ChangeNumServiceImpl.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/component/biz/impl/mine/ChangeProfileBackgroundActivity$onCreate$1$2$1$1$1.smali` | 5 | 0 | 2 | 7 |
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
| `com/dragon/read/component/biz/impl/mine/dc$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/component/biz/impl/mine/gf.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/hc.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/ig.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/kc.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/component/biz/impl/mine/l8.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/nc.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/pc.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/r9.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/we.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/wf.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/x8.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/component/biz/impl/mine/ye.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/FixRefreshBottomTab.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$b.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$i.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$w.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainFragmentActivity$y.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$a.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$c.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/pages/main/MiraCastMonitor$c.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/pages/main/a3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/f.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/g1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/i0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/k3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/m0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/m3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/p0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/q0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/r0.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/pages/main/s.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/reader/ad/ReaderAdManager$d.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/reader/ad/a0$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/reader/ad/noad/InspireNoAdsDialog$Companion$a.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/CoroutineExecutor.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/FrequencyMgr$Period$Never.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$b$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$j.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/ImageLoaderUtils$q.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/PremiumReportHelper$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/util/UiConfigSetter$n$a.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/ViewStatusUtils.smali` | 2 | 0 | 5 | 7 |
| `com/dragon/read/util/b5$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/util/b6.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/bb$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/d7$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/db.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/e2.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/eb.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/h3.smali` | 1 | 0 | 6 | 7 |
| `com/dragon/read/util/h7.smali` | 3 | 0 | 4 | 7 |
| `com/dragon/read/util/h9.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/i4.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/ja.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/k0$a.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/k0.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/k7.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/ka.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/o1.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/o4.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/o5.smali` | 2 | 0 | 5 | 7 |
| `com/dragon/read/util/q5.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/q9.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/s1.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/ta.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/v3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/v7$a.smali` | 6 | 0 | 1 | 7 |
| `com/dragon/read/util/w.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/w3.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/x3.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/y1.smali` | 4 | 0 | 3 | 7 |
| `com/dragon/read/util/y2.smali` | 5 | 0 | 2 | 7 |
| `com/dragon/read/util/z5.smali` | 5 | 0 | 2 | 7 |
| `com/ss/android/update/e0.smali` | 2 | 0 | 5 | 7 |
| `com/ss/android/update/j.smali` | 4 | 0 | 3 | 7 |
| `com/ss/android/update/n.smali` | 2 | 0 | 5 | 7 |
| `com/ss/android/update/q$b.smali` | 5 | 0 | 2 | 7 |
| `com/ss/android/update/s.smali` | 3 | 0 | 4 | 7 |
| `com/ss/android/update/t$a.smali` | 5 | 0 | 2 | 7 |
| `com/tencent/tinker/android/dx/instruction/InstructionPromoter.smali` | 0 | 0 | 7 | 7 |
| `com/tencent/tinker/android/dx/instruction/InstructionWriter.smali` | 0 | 0 | 7 | 7 |
| `com/unionpay/a.smali` | 0 | 0 | 7 | 7 |
| `yx2/v.smali` | 0 | 0 | 7 | 7 |
| `yy2/i.smali` | 0 | 0 | 7 | 7 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayConfirmFragment.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a0.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$homePageAction$2$1.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/payagain/applog/StdPayAgainMainLogger.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyFaceVM.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0$e.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/ttcjpayapi/CJPayCarrierAuthManager.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/verify/utils/e.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/verify/utils/h.smali` | 0 | 0 | 6 | 6 |
| `com/dragon/read/ad/util/UserRegionAdUtil.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/ad/util/a$a.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/ad/util/e1.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/ad/util/l.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/ad/util/n.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/ad/util/v0.smali` | 4 | 0 | 2 | 6 |
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
| `com/dragon/read/component/biz/impl/mine/ae.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ag.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/b9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/fb.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/fc.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/fe.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/fg.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/g9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/hb.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/ia.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c$c.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/n9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/p8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/pd.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/q8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/r7.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/rc.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/rd.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/s9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/sg.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/t9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/tc.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/uf.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/w8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/xa.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/component/biz/impl/mine/z9.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/MainFragmentActivity$c0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/MainFragmentActivity$e0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/a0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/a4$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/a5.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/b0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/c2.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/pages/main/f3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/l3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/n3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/o.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/p4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/q1.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/r4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/s2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/s4$a.smali` | 1 | 0 | 5 | 6 |
| `com/dragon/read/pages/main/t4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/v4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/w0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/x2.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/pages/main/y.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/y2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/y3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/pages/main/z2.smali` | 4 | 0 | 2 | 6 |
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
| `com/dragon/read/util/ImageLoaderUtils$n.smali` | 1 | 0 | 5 | 6 |
| `com/dragon/read/util/PictureUtils$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/PictureUtils$j.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/RouterUtils.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/RxUtils$c$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/UiConfigSetter$c.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/UiConfigSetter$l.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/a4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/a7.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/aa.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/b9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ba.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/c9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ca.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/d.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/d2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/da.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/e0.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/e5.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/e9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/f$d.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/f4.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/f9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/fa.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/g9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ga.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ha.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/hb.smali` | 1 | 0 | 5 | 6 |
| `com/dragon/read/util/i9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ia.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ib.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/j9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/la.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/lb.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/m.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/n.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/n0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/o.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/o0.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/o3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/o7.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/p2.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/p8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/p9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/q3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/q7.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/r7.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/r9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/s0.smali` | 2 | 0 | 4 | 6 |
| `com/dragon/read/util/s3.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/s4.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/s9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/t7$a.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/t8.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/t9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/u.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/u5.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/ua.smali` | 4 | 0 | 2 | 6 |
| `com/dragon/read/util/v9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/w9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/x8.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/x9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/y9.smali` | 3 | 0 | 3 | 6 |
| `com/dragon/read/util/ya.smali` | 3 | 0 | 3 | 6 |
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
| `com/tencent/tauth/Tencent.smali` | 0 | 0 | 6 | 6 |
| `xc/e.smali` | 0 | 0 | 6 | 6 |
| `xf/f.smali` | 0 | 0 | 6 | 6 |
| `xl2/e.smali` | 0 | 0 | 6 | 6 |
| `xx2/d$a.smali` | 0 | 0 | 6 | 6 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper$y.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayHomePageUIModule.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/BaseStandardHomeFragment.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b.smali` | 0 | 0 | 5 | 5 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/e.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/alliance/settings/AllianceOnlineSettings$$SettingImpl.smali` | 0 | 0 | 5 | 5 |
| `com/bytedance/android/ad/sdk/impl/advideo/monitor/AdVideoMonitorUtils.smali` | 0 | 0 | 5 | 5 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$WXJumpInfoResponse$DataModel.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$WXJumpInfoResponse.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/b1$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/ad/util/c.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/f0.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/ad/util/r.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/ad/util/w.smali` | 3 | 0 | 2 | 5 |
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
| `com/dragon/read/component/biz/impl/mine/a2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/a6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ab.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/b8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/bd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/bg.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/c6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/cd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/cg.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/d6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/dd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/e6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ed.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/f6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/fc$a.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/component/biz/impl/mine/fd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/g7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ga.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/h6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ha.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/i6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ib.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/j7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ja.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/jc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/k6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/l6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c$a.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/i.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/component/biz/impl/mine/m2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/m7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/n8.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/o6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/oa.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/component/biz/impl/mine/p2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/p6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/q9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/qa.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/r6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/rb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/s6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/sb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/sd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/t7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/u9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ug.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/v6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/vb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/w9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/wc.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/x9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/xd.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/y9.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/z5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/za.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/component/biz/impl/mine/ze.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/MainFragmentActivity$d.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/MainFragmentActivity$n.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$SavedState.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$d.smali` | 1 | 0 | 4 | 5 |
| `com/dragon/read/pages/main/c3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/c4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/d.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/f4$a.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/pages/main/g3$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/pages/main/j3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/k4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/l0.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/r.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/t.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/t0.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/t1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/u.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/u0.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/u1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/pages/main/v1.smali` | 3 | 0 | 2 | 5 |
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
| `com/dragon/read/util/a6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/b2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/d9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/f$b.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/f$f.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/g.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/g3.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/gb.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/h6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/i6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/j2.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/j4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/j6.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/jb.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/k9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/l5$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/util/l9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/m$a.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/m$b.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/m9.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/ma.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/mb.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/n5$a.smali` | 4 | 0 | 1 | 5 |
| `com/dragon/read/util/p7.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/pa$a.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/q1.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/t1.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/t2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/t4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/t5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/u4.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/v6.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/v7.smali` | 2 | 0 | 3 | 5 |
| `com/dragon/read/util/w5.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/w7.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/wa.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/x2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/z2.smali` | 3 | 0 | 2 | 5 |
| `com/dragon/read/util/z8.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/UpdateProgressActivity$f.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/d0.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/s$a.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/u$d.smali` | 2 | 0 | 3 | 5 |
| `com/ss/android/update/z$g.smali` | 1 | 0 | 4 | 5 |
| `com/ss/videoarch/liveplayer/PreloadHelper$PreloadEventHandler.smali` | 0 | 0 | 5 | 5 |
| `com/vivo/push/util/NotifyAdapterUtil.smali` | 0 | 0 | 5 | 5 |
| `do/c$a.smali` | 0 | 0 | 5 | 5 |
| `hl/d$a.smali` | 0 | 0 | 5 | 5 |
| `p8/f.smali` | 0 | 0 | 5 | 5 |
| `tj/a.smali` | 0 | 0 | 5 | 5 |
| `wj/b.smali` | 0 | 0 | 5 | 5 |
| `zd/b.smali` | 0 | 0 | 5 | 5 |
| `zd/c.smali` | 0 | 0 | 5 | 5 |
| `a42/o.smali` | 0 | 0 | 4 | 4 |
| `an2/e.smali` | 1 | 0 | 3 | 4 |
| `com/android/ttcjpaysdk/fastpay/activity/FastPayActivity.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/integrated/counter/component/view/DYPayViewProvider.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayCompleteFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayConfirmFragment$b.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayMethodFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/counter/activity/CJPayCheckoutCounterActivity.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/n.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/result/PayResultFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/features/b.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/a.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/i.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/y.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/q$d.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/j.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/FrontMethodFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/FrontRetryCombinePayFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainGuideFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/e.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/l.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/g.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSSmsVerifyFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/utils/CreditPayProcessUtils.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/VerifyPayTypeWithCombineWrapper.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l1.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/o0.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p0.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/p1.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/verify/jsb/c.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/verify/view/fragment/DyVerifySmsFragment.smali` | 0 | 0 | 4 | 4 |
| `com/android/ttcjpaysdk/verify/vm/DyVerifyFingerprintVM.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/services/impl/h.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/services/impl/t.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/settings/AllianceMultiProcessLocalSetting$$SettingImpl.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/alliance/utils/Utils.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/android/ad/preload/session/i.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/apm/agent/instrumentation/okhttp3/OkHttpRecord.smali` | 0 | 0 | 4 | 4 |
| `com/bytedance/ies/sdk/widgets/api/WidgetService.smali` | 0 | 0 | 4 | 4 |
| `com/dragon/read/ad/util/l0.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/ad/util/o.smali` | 2 | 0 | 2 | 4 |
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
| `com/dragon/read/component/biz/impl/mine/a7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/a9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/aa.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/bb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/bc.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/c7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/c9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/cc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ce.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/d8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/db.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ea.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ec.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ee.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/f.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/f8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/gb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/gc.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/gd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/h.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/h9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/i.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/i7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ic.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ie.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/j9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/jb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/k8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/la.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/lb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c$d.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/g.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/h.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/component/biz/impl/mine/m8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/m9.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/mc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/md.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/o8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ob.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/oc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/od.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/p7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/pb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/q7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/qc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/qd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/qe.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/re.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/rg.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/sc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/tb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/u7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ub.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/uc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/ve.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/vf.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/w7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/wb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/xf.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/y7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/y8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/yb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/yc.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/zb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/component/biz/impl/mine/zd.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$f0.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$k.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$p.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$t.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$u.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$v.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainFragmentActivity$z.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$b.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/pages/main/a4$b$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/b1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/b3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/b5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/c0.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/d1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/d2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/e1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/e3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/e4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/f0.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/f1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/g4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/h1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/h4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/i1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/i2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/i4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/j1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/p2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/p3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/q2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/q3$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/r2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/r3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/s1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/s3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/t2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/t3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/u3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/u4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/v0.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/w4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/x2$a$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/x4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/y1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/y2$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/z1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/z3$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/pages/main/z4.smali` | 2 | 0 | 2 | 4 |
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
| `com/dragon/read/util/ab$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/ab.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/b1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/b4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/bb.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/c3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/c4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/c5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/c6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/d1.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/d3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/e6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/e8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/f$e.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/f7$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/fa$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/g8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/h2$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/h2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/i1.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/i7$b.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/i7$c.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/i7$d.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/j0.smali` | 1 | 0 | 3 | 4 |
| `com/dragon/read/util/j3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/j7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/k6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/l4$a.smali` | 3 | 0 | 1 | 4 |
| `com/dragon/read/util/n3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/n7.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/o2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/oa.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/p3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/q.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/q2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/qa$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/r3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/r5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/s2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/s6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/t3.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/t6.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/u8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/u9$a.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/v2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/v5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/v8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/w2.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/w8.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/x4.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/y5.smali` | 2 | 0 | 2 | 4 |
| `com/dragon/read/util/z6.smali` | 1 | 0 | 3 | 4 |
| `com/ss/android/update/MaxSizeLinearLayout.smali` | 1 | 0 | 3 | 4 |
| `com/ss/android/update/UpdateCheckerService$1.smali` | 2 | 0 | 2 | 4 |
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
| `com/ss/android/update/z$d.smali` | 2 | 0 | 2 | 4 |
| `com/ss/videoarch/live/ttquic/PreloadManager.smali` | 0 | 0 | 4 | 4 |
| `com/ss/videoarch/strategy/dataCenter/strategyData/NodeTableOperate.smali` | 0 | 0 | 4 | 4 |
| `com/ss/videoarch/strategy/strategy/smartStrategy/SuperResolution.smali` | 0 | 0 | 4 | 4 |
| `com/tencent/connect/share/QQShare.smali` | 0 | 0 | 4 | 4 |
| `com/tencent/mm/opensdk/openapi/WXAPiSecurityHelper.smali` | 0 | 0 | 4 | 4 |
| `com/tencent/open/utils/m.smali` | 0 | 0 | 4 | 4 |
| `com/tencent/tinker/lib/MuteInstaller.smali` | 0 | 0 | 4 | 4 |
| `com/tencent/tinker/lib/utils/DirUtils.smali` | 0 | 0 | 4 | 4 |
| `com/tencent/tinker/lib/utils/ShareTinkerInternals.smali` | 0 | 0 | 4 | 4 |
| `com/ttnet/org/chromium/net/AndroidNetworkLibrary.smali` | 0 | 0 | 4 | 4 |
| `com/ttreader/tthtmlparser/TTEpubLayoutManager.smali` | 0 | 0 | 4 | 4 |
| `kn/i.smali` | 0 | 0 | 4 | 4 |
| `oe/h$a.smali` | 0 | 0 | 4 | 4 |
| `q30/k.smali` | 0 | 0 | 4 | 4 |
| `uc/a.smali` | 0 | 0 | 4 | 4 |
| `z60/a.smali` | 0 | 0 | 4 | 4 |
| `zd/a.smali` | 0 | 0 | 4 | 4 |
| `zd/d.smali` | 0 | 0 | 4 | 4 |
| `zv2/e.smali` | 0 | 0 | 4 | 4 |
| `a52/a.smali` | 0 | 0 | 3 | 3 |
| `bg/c.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/bindcard/base/pay/CJPayNewCardActivity.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/facelive/data/FaceVerifyParams.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/integrated/counter/component/view/std/StdAssetPayViewProvider.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/integrated/counter/component/view/std/StdBytePayViewProvider.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/integrated/counter/component/view/std/StdNonBytePayViewProvider.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/fragment/CJPayCombineFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRBankCardActivity.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayFingerprintGuideFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/directbank/DirectBankActivity.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/process/PayResultProcess.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/wrapper/DyPayCoreWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayHomePageMethodModule$initMethodView$selectMethodCallback$1.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyCarrierVM.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$authFingerprint$1.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/e$d.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/m$b.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/o.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/t.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPrePayProcess.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/e.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/q.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayCommonUtils$a.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/b.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMainFragment$d.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMethodFragment.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/p.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/proxy/q.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/DynamicPwdWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/PwdBaseWrapper.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/y.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/c.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/m1.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/o1.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/r0.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/b.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/verify/activity/DyStepUpIFrameActivity.smali` | 0 | 0 | 3 | 3 |
| `com/android/ttcjpaysdk/verify/utils/DyVerifyCertOperate.smali` | 0 | 0 | 3 | 3 |
| `com/awesome/fqhybrid/core/FqAnnieXCardLynxEngineProxy.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/alliance/services/impl/d.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/alliance/services/impl/r0.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/android/ad/sdk/impl/ipc/AdIpcDepend.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/apm/ApmContext.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/apm/block/m.smali` | 0 | 0 | 3 | 3 |
| `com/bytedance/ies/sdk/widgets/priority/PriorityManager.smali` | 0 | 0 | 3 | 3 |
| `com/dragon/read/ad/util/a0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/c0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/c1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/d0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/d1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/e0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/ad/util/l0$a.smali` | 1 | 0 | 2 | 3 |
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
| `com/dragon/read/component/biz/impl/mine/b0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/b1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/b7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/bf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/c8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/card/model/QuickAccessCard$updateTrebleFuncLayout$gridLayoutManager$1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/cf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/d0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/d1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/d7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/df.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/dg.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/e7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/f0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/f1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/fa.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/g0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/g1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/gg.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/h8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/hd.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/i0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/i1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/i8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/j0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/j1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/je.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/jf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/jg.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/k7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ka.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/ke.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/l0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/l1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/le.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/m0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/m1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/mc$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/me.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/n1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/o.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/o0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/o1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/p.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/p0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/p1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/pa.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/pf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/q.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/q0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/q1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/r0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/r1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/s1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/t.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/t0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/t1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/td.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/te.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/u8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v5.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/component/biz/impl/mine/v8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/v9.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/w.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/w0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/w1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/wa.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/x.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/x0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/x1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/y1.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/component/biz/impl/mine/yd.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/yf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/z8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/zc.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/component/biz/impl/mine/zf.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/FixRefreshBottomTab$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$g.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$j.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$l.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$m.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/MainFragmentActivity$o.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/a1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/a2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/a4$b$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/d4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/e0$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/e0$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/f2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/j0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/k0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/k2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/m1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/m4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/n4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/o3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/w2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/x3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/y0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/z0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/pages/main/z3$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/ReaderAdManager$h.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/g.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/h$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/reader/ad/i$a.smali` | 1 | 0 | 2 | 3 |
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
| `com/dragon/read/util/b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/b5.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/c8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/d$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/e7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/f$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/f0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/f3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/f8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/g4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/g7.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/h1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/i7$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/i7$e.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/i7$f.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/i8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/j2$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/j8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/k$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/k8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/l8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/m2.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n$b.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n$c.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/n6.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/o6.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/o8.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/p.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/q4.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/r1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/r8$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/ra.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/u3$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/u3.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/v0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/w0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/x.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/x6.smali` | 2 | 0 | 1 | 3 |
| `com/dragon/read/util/xa.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z$a.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z0.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z1.smali` | 1 | 0 | 2 | 3 |
| `com/dragon/read/util/z7$b.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/b0.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/i0.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/m.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/o$a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/q$d.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/t$c.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/u$c.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/w$a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/w.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/x$a.smali` | 1 | 0 | 2 | 3 |
| `com/ss/android/update/z$c.smali` | 1 | 0 | 2 | 3 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerVideoEffectManager.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/strategy/dataCenter/strategyData/ConfigTableOperate.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/strategy/dataCenter/strategyData/HistoryTableOperate.smali` | 0 | 0 | 3 | 3 |
| `com/ss/videoarch/strategy/strategy/nodeOptimizer/DnsOptimizer.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/connect/auth/a.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/connect/avatar/ImageActivity.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/connect/common/UIListenerManager.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/mm/opensdk/openapi/MMSharedPreferences.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/mm/opensdk/openapi/WXApiImplComm.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/open/a/b.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/open/b/b.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/tinker/lib/MuteExpHandler.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/tinker/lib/dexopt/DexOptimize.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/tinker/lib/hook/MuteInstrumentation.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/tinker/lib/signature/ApkSignatureVerify.smali` | 0 | 0 | 3 | 3 |
| `com/tencent/tinker/loader/MuteApplication.smali` | 0 | 0 | 3 | 3 |
| `com/unionpay/UPPayWapActivity.smali` | 0 | 0 | 3 | 3 |
| `com/unionpay/utils/UPUtils.smali` | 0 | 0 | 3 | 3 |
| `com/vivo/push/util/m.smali` | 0 | 0 | 3 | 3 |
| `d60/j.smali` | 0 | 0 | 3 | 3 |
| `d8/a$a.smali` | 0 | 0 | 3 | 3 |
| `e8/c.smali` | 0 | 0 | 3 | 3 |
| `eb/g.smali` | 0 | 0 | 3 | 3 |
| `fb/e.smali` | 0 | 0 | 3 | 3 |
| `la/a.smali` | 0 | 0 | 3 | 3 |
| `n20/a.smali` | 0 | 0 | 3 | 3 |
| `n60/d.smali` | 0 | 0 | 3 | 3 |
| `nd/j.smali` | 0 | 0 | 3 | 3 |
| `oe/g.smali` | 0 | 0 | 3 | 3 |
| `oe/h.smali` | 0 | 0 | 3 | 3 |
| `q20/a.smali` | 0 | 0 | 3 | 3 |
| `qe/c.smali` | 0 | 0 | 3 | 3 |
| `qq/g.smali` | 0 | 0 | 3 | 3 |
| `t20/i.smali` | 0 | 0 | 3 | 3 |
| `u60/c$a.smali` | 0 | 0 | 3 | 3 |
| `ui/l.smali` | 0 | 0 | 3 | 3 |
| `v52/b.smali` | 0 | 0 | 3 | 3 |
| `wd/a.smali` | 0 | 0 | 3 | 3 |
| `wi/f.smali` | 0 | 0 | 3 | 3 |
| `xc/c.smali` | 0 | 0 | 3 | 3 |
| `z43/k.smali` | 0 | 0 | 3 | 3 |
| `a02/m.smali` | 0 | 0 | 2 | 2 |
| `a82/b0$a.smali` | 0 | 0 | 2 | 2 |
| `a82/c.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/contacts/ContactsPickerDialog.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/j.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/k.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/h5/utils/m.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/ui/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/ui/component/dialog/CJCommonDialog.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/base/utils/CJPayBasicUtils.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/bdpay/bindcard/lynx/CJPayLynxMyBankCardProvider.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/bindcard/base/ui/CJPayVCRExceptionFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/bindcard/base/ui/CJPayVerificationCodeFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/facelive/core/e.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/facelive/utils/c.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/facelive/view/panel/e.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/integrated/counter/activity/IntegratedCounterActivity.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/integrated/counter/component/view/ATPayViewProvider.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/wrapper/ConfirmLynxCardWrapper.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/integrated/counter/utils/CJPayCommonParamsBuildUtils$Companion.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/medicalpay/b$a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRIdentityActivity.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/agreement/fragment/CJPayAgreementDetailFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/agreement/fragment/CJPayAgreementFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayBdPayContinuePayGuideFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayPasswordRelatedGuideFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/FastPayMoreFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/process/VerifyProcess.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper$pageMonitor$2$1.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/b.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/l.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/q.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/t.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/CJUnifyAssetItemView.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/CJUnifyHalfMethodDialog.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/k.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$b.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a$d.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/UnifyPreVerifyBaseVM.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/e.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/d0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/t$b.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/v.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/x.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/m.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/n.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/j$c.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardPayTypeWrapper.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/g.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/f.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/CJUnifyPayEventUtils.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/CJUnifyPayCommonHttpParamsUtil.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/g.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/q.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/payagain/presenter/b$a.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/activity/CJPaySSSmsVerifyActivity.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/activity/CJPaySSUpdateCardInfoActivity.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyAgreementDetailFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyFingerPrintPreHalfWindowFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifySmsFullFragment.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/VerifyOneStepPaymentVM$e.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/h.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/i.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/k.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/l0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/m0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/s0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/w0.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/verify/vm/z0$i.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/AudioHelper.smali` | 0 | 0 | 2 | 2 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/SAMICoreDeNoise.smali` | 0 | 0 | 2 | 2 |
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
| `com/android/ttcjpaysdk/verify/vm/e.smali` | 0 | 0 | 2 | 2 |
| `com/awesome/fqhybrid/bridge/impl/f.smali` | 0 | 0 | 2 | 2 |
| `com/awesome/fqhybrid/service/FqLynxBizService$b.smali` | 0 | 0 | 2 | 2 |
| `com/awesome/fqhybrid/service/FqLynxBizService.smali` | 0 | 0 | 2 | 2 |
| `com/byted/mgl/merge/service/api/share/BdpShareBaseInfo.smali` | 0 | 0 | 2 | 2 |
| `com/byted/mgl/merge/service/api/share/ShareImCallbackInfo.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/ad/live/component/sif/lynxbridge/d0.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$2.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$config$1$getNextInspireCallback$1.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$config$1$launchRequestNextRewardInfo$1.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/AdEventImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/InspireAdInitConfigImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/InspireAdRequestImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/admetaversesdk/inspire/impl/NetworkImpl.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/alliance/bean/PassData.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/bridges/log/SifLog$a.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/reward/dynamicad/AbsRewardLynxFragment$b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/rewarded/draw/DrawAdLoadMoreDispatcher.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/rewarded/draw/RewardAdDrawFragment$b.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/sdk/api/ipc/AbsAdIpcAsyncMethod.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceCapabilityFactory.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/anniex/bd/foundation/impl/s.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/instrumentation/ClickInstrumentation.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/instrumentation/okhttp3/OkHttpEventListener.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/instrumentation/transaction/TxState.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/agent/v2/instrumentation/ClickAgent.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/config/ApmStartConfig$Builder.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/internal/ApmDelegate.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/util/CommonMonitorUtil.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/apm/util/TrafficUtils.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/applog/et_verify/EventVerify.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/applog/priority/original/w.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/article/common/utils/ConcaveScreenUtils.smali` | 0 | 0 | 2 | 2 |
| `com/bytedance/ies/sdk/widgets/WidgetManager.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/base/AbsActivity.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/component/biz/impl/ab/IXraySwitch$$Impl.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragment$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/HongguoMineFragmentV2$initFunctionListWithSideBar$1.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/KmpHongguoMineFragment$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/NewChangeProfileActivity$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$i.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/VariantMineFragment$k.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/f7$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/he.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/kb$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/lc.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/LoginTypeView$ShowType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/a$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/b$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/c$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/d$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/f$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/j$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/k$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/l$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/IFixRefreshBottomTab$$Impl$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/MainFragmentActivity$e.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/MainPageDrawerLayout$SavedState$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/MiraCastMonitor$JudgmentType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/pages/main/MiraCastMonitor$MiraCastState.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/pages/main/b2.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/g$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/m2.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/n2.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/s0.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/v3.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/pages/main/z$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/reader/ad/a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/reader/ad/p.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/user/model/NetIdLoginResp$Status.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/CdnImageCacheEventListener$Scene.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/CustomFrescoMonitor$DownSampleType.smali` | 0 | 0 | 2 | 2 |
| `com/dragon/read/util/DragonRequestController$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/KeyBoardHelper$OnKeyBoardListener$-CC.smali` | 1 | 0 | 1 | 2 |
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
| `com/dragon/read/util/a5.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/c.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/c2$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/e.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/h7$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/i3.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/k0$b.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/l.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/n4.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/n5.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/n7$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/r6.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/s7.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/u0.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/u1.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/v1.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/w1$a.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/x7.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/y4.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/y6.smali` | 1 | 0 | 1 | 2 |
| `com/dragon/read/util/z7$a.smali` | 1 | 0 | 1 | 2 |
| `com/minigame/miniapphost/AppBrandLogger.smali` | 0 | 0 | 2 | 2 |
| `com/ss/android/update/g.smali` | 1 | 0 | 1 | 2 |
| `com/ss/android/update/i$b.smali` | 1 | 0 | 1 | 2 |
| `com/ss/android/update/j0$a.smali` | 1 | 0 | 1 | 2 |
| `com/ss/videoarch/live/LiveIOWrapper.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/effect/VeLivePlayerVideoEffectManager.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/log/LiveApplog.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/liveplayer/log/LiveError.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/strategy/LiveStrategyManager.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/strategy/dataCenter/config/LSSettings.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/strategy/dataCenter/strategyData/BaseTableOperate.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/strategy/network/NetworkMonitorLoader.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/strategy/strategy/liveio/LiveIOEngine.smali` | 0 | 0 | 2 | 2 |
| `com/ss/videoarch/strategy/strategy/smartStrategy/BaseSmartStrategy.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/a/a.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/auth/AuthAgent$b.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/auth/AuthAgent.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/auth/a$a.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/avatar/ImageActivity$5.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/avatar/QQAvatar.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/share/QQShare$2.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/share/QzonePublish.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/connect/share/QzoneShare.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelbiz/WXChannelBaseJumpInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelbiz/WXChannelJumpMiniProgramInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelbiz/WXChannelJumpUrlInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelmsg/WXMusicVipInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelmsg/WXStateJumpChannelProfileInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelmsg/WXStateJumpMiniProgramInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mm/opensdk/modelmsg/WXStateJumpUrlInfo.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/mmkv/MMKV.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/open/SocialApiIml.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/open/b/a.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/open/log/b.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/lib/MuteInstallClient.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/lib/MuteResReplacer.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/lib/dexopt/DexAlign.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/lib/hook/ContentProviderProxy$CrudProviderMethod.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/lib/hook/MuteHandlerCallback.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/lib/utils/ResTranUtils.smali` | 0 | 0 | 2 | 2 |
| `com/tencent/tinker/loader/utils/DirUtils.smali` | 0 | 0 | 2 | 2 |
| `com/tiktok/ttm/TTMOutput.smali` | 0 | 0 | 2 | 2 |
| `com/tt/android/qualitystat/config/QualityPreference.smali` | 0 | 0 | 2 | 2 |
| `com/tt/miniapphost/AppBrandLogger.smali` | 0 | 0 | 2 | 2 |
| `com/ttnet/org/chromium/base/BuildInfo.smali` | 0 | 0 | 2 | 2 |
| `com/ttnet/org/chromium/net/impl/CronetUrlRequestContext.smali` | 0 | 0 | 2 | 2 |
| `com/ttnet/org/chromium/net/urlconnection/CronetHttpURLConnection.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/b/x.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/h/ai.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/n.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/util/ContextDelegate.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/util/ad.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/util/ak.smali` | 0 | 0 | 2 | 2 |
| `com/vivo/push/util/o.smali` | 0 | 0 | 2 | 2 |
| `d40/d.smali` | 0 | 0 | 2 | 2 |
| `d60/d.smali` | 0 | 0 | 2 | 2 |
| `d60/h.smali` | 0 | 0 | 2 | 2 |
| `dl/i0.smali` | 0 | 0 | 2 | 2 |
| `dl/j0.smali` | 0 | 0 | 2 | 2 |
| `e40/g.smali` | 0 | 0 | 2 | 2 |
| `e70/f.smali` | 0 | 0 | 2 | 2 |
| `eh/f.smali` | 0 | 0 | 2 | 2 |
| `eh/k.smali` | 0 | 0 | 2 | 2 |
| `el/e.smali` | 0 | 0 | 2 | 2 |
| `en/f.smali` | 0 | 0 | 2 | 2 |
| `f9/c$b.smali` | 0 | 0 | 2 | 2 |
| `f9/c$f.smali` | 0 | 0 | 2 | 2 |
| `f9/f.smali` | 0 | 0 | 2 | 2 |
| `f9/g.smali` | 0 | 0 | 2 | 2 |
| `f9/n.smali` | 0 | 0 | 2 | 2 |
| `f9/o.smali` | 0 | 0 | 2 | 2 |
| `fb/g.smali` | 0 | 0 | 2 | 2 |
| `fp/a$a.smali` | 0 | 0 | 2 | 2 |
| `g40/b.smali` | 0 | 0 | 2 | 2 |
| `gh/a$a.smali` | 0 | 0 | 2 | 2 |
| `h9/d$a.smali` | 0 | 0 | 2 | 2 |
| `hb/c.smali` | 0 | 0 | 2 | 2 |
| `i40/d.smali` | 0 | 0 | 2 | 2 |
| `i40/e$c.smali` | 0 | 0 | 2 | 2 |
| `ih/a.smali` | 0 | 0 | 2 | 2 |
| `ii/b.smali` | 0 | 0 | 2 | 2 |
| `ii/d.smali` | 0 | 0 | 2 | 2 |
| `ip/a.smali` | 0 | 0 | 2 | 2 |
| `jb/h.smali` | 0 | 0 | 2 | 2 |
| `jp/b.smali` | 0 | 0 | 2 | 2 |
| `k8/a.smali` | 0 | 0 | 2 | 2 |
| `k80/h.smali` | 0 | 0 | 2 | 2 |
| `kk/a.smali` | 0 | 0 | 2 | 2 |
| `la/e.smali` | 0 | 0 | 2 | 2 |
| `lf/a.smali` | 0 | 0 | 2 | 2 |
| `ma/c.smali` | 0 | 0 | 2 | 2 |
| `mf/a.smali` | 0 | 0 | 2 | 2 |
| `oc/a.smali` | 0 | 0 | 2 | 2 |
| `oi/c.smali` | 0 | 0 | 2 | 2 |
| `pa/a.smali` | 0 | 0 | 2 | 2 |
| `q30/d$a.smali` | 0 | 0 | 2 | 2 |
| `q40/b.smali` | 0 | 0 | 2 | 2 |
| `qf/f.smali` | 0 | 0 | 2 | 2 |
| `qi/c.smali` | 0 | 0 | 2 | 2 |
| `qi/d$a.smali` | 0 | 0 | 2 | 2 |
| `qi/d$b.smali` | 0 | 0 | 2 | 2 |
| `qi/d$e.smali` | 0 | 0 | 2 | 2 |
| `qi/d.smali` | 0 | 0 | 2 | 2 |
| `qi/f.smali` | 0 | 0 | 2 | 2 |
| `rq/a.smali` | 0 | 0 | 2 | 2 |
| `sa/a.smali` | 0 | 0 | 2 | 2 |
| `t20/g.smali` | 0 | 0 | 2 | 2 |
| `t20/k.smali` | 0 | 0 | 2 | 2 |
| `tj/f.smali` | 0 | 0 | 2 | 2 |
| `u60/d.smali` | 0 | 0 | 2 | 2 |
| `u60/e.smali` | 0 | 0 | 2 | 2 |
| `uc/a$a.smali` | 0 | 0 | 2 | 2 |
| `ui/d.smali` | 0 | 0 | 2 | 2 |
| `um/c.smali` | 0 | 0 | 2 | 2 |
| `vq/a.smali` | 0 | 0 | 2 | 2 |
| `w8/a.smali` | 0 | 0 | 2 | 2 |
| `wr2/u.smali` | 0 | 0 | 2 | 2 |
| `wz2/e.smali` | 0 | 0 | 2 | 2 |
| `wz2/h.smali` | 0 | 0 | 2 | 2 |
| `x40/d.smali` | 0 | 0 | 2 | 2 |
| `x60/d.smali` | 0 | 0 | 2 | 2 |
| `xk2/b.smali` | 0 | 0 | 2 | 2 |
| `xk2/c.smali` | 0 | 0 | 2 | 2 |
| `xo2/f.smali` | 0 | 0 | 2 | 2 |
| `z23/f.smali` | 0 | 0 | 2 | 2 |
| `z30/b.smali` | 0 | 0 | 2 | 2 |
| `z43/v.smali` | 0 | 0 | 2 | 2 |
| `z53/e.smali` | 0 | 0 | 2 | 2 |
| `zd/f.smali` | 0 | 0 | 2 | 2 |
| `zx2/a.smali` | 0 | 0 | 2 | 2 |
| `zx2/l.smali` | 0 | 0 | 2 | 2 |
| `a02/d.smali` | 0 | 0 | 1 | 1 |
| `a02/j.smali` | 0 | 0 | 1 | 1 |
| `a02/n.smali` | 0 | 0 | 1 | 1 |
| `a42/g.smali` | 0 | 0 | 1 | 1 |
| `a42/h.smali` | 0 | 0 | 1 | 1 |
| `a42/i.smali` | 0 | 0 | 1 | 1 |
| `a42/k.smali` | 0 | 0 | 1 | 1 |
| `a42/p.smali` | 0 | 0 | 1 | 1 |
| `a48/b.smali` | 0 | 0 | 1 | 1 |
| `a52/a$a.smali` | 0 | 0 | 1 | 1 |
| `a68/c.smali` | 0 | 0 | 1 | 1 |
| `a82/a.smali` | 0 | 0 | 1 | 1 |
| `a82/a0.smali` | 0 | 0 | 1 | 1 |
| `a82/b0$a$a$a.smali` | 0 | 0 | 1 | 1 |
| `a82/b0$a$b$a.smali` | 0 | 0 | 1 | 1 |
| `a82/e0.smali` | 0 | 0 | 1 | 1 |
| `a82/s.smali` | 0 | 0 | 1 | 1 |
| `a82/t.smali` | 0 | 0 | 1 | 1 |
| `a82/u.smali` | 0 | 0 | 1 | 1 |
| `a82/y$b.smali` | 0 | 0 | 1 | 1 |
| `a82/y.smali` | 0 | 0 | 1 | 1 |
| `a88/d.smali` | 0 | 0 | 1 | 1 |
| `a88/h.smali` | 0 | 0 | 1 | 1 |
| `a93/d0$a.smali` | 0 | 0 | 1 | 1 |
| `a93/d0.smali` | 0 | 0 | 1 | 1 |
| `a93/g0.smali` | 0 | 0 | 1 | 1 |
| `a93/i.smali` | 0 | 0 | 1 | 1 |
| `a93/j.smali` | 0 | 0 | 1 | 1 |
| `a93/m.smali` | 0 | 0 | 1 | 1 |
| `aa2/a$a.smali` | 0 | 0 | 1 | 1 |
| `aa8/a.smali` | 0 | 0 | 1 | 1 |
| `aa8/b.smali` | 0 | 0 | 1 | 1 |
| `aa8/c.smali` | 0 | 0 | 1 | 1 |
| `ab/a.smali` | 0 | 0 | 1 | 1 |
| `b38/c.smali` | 0 | 0 | 1 | 1 |
| `b38/d.smali` | 0 | 0 | 1 | 1 |
| `b58/b.smali` | 0 | 0 | 1 | 1 |
| `be/b.smali` | 0 | 0 | 1 | 1 |
| `bg/d.smali` | 0 | 0 | 1 | 1 |
| `c38/a$b.smali` | 0 | 0 | 1 | 1 |
| `c88/b.smali` | 0 | 0 | 1 | 1 |
| `c88/y0.smali` | 0 | 0 | 1 | 1 |
| `cg/a.smali` | 0 | 0 | 1 | 1 |
| `ci/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/CJPayPerformance$Module.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/CJPayTrackReport$FrontCounterSubSectionEnum.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/CJPayTrackReport$Scenes.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/encrypt/CJPayEncryptHelper$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/framework/AnimUtil$AnimGroup.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/framework/AnimUtil$ErrorType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/framework/BaseFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/framework/container/view/components/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/framework/container/view/components/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/JSBBioVerify$realHandle$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/a0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/f1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/t.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/utils/i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/x.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/y.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/cjjsb/z.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/ui/LynxActivity$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/h5/utils/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/DyVerifyFlow.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayCombineService$CombinePayErrorType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayCombineService$CombineType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayDyVerifyService$IDyVerifyCallback$CertStageType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayDyVerifyService$IDyVerifyCallback$DyVerifyProductStageStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayFaceCheckCallback$FaceStageStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayFaceCheckCallback$FaceStageType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayFaceCheckService$Companion.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayNormalBindCardService$BindCardType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayNormalBindCardService$BizType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPayNormalBindCardService$SourceType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/ICJPaySecurityLoadingService$SecurityLoadingScene.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/PayMsg.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/service/bean/DyPayProcessConfig$Scenes.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/settings/bean/CJPayFaceVerifyConfig$CJPayFaceResultConfig.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/settings/bean/CJPaySignBizConfig$CJPayConfirmNeedCheckAgainConfig$CJPayAlertContents.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/smart/CJPaySmartTemperatureHelper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/Utils/f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/component/dialog/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/component/input/CJPwdInputLayout.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/data/CJPayTopRightBtnInfo.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/data/JumpInfoBean$Action.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/dialog/CJPayDialogBuilder$DialogStyle.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/dialog/a0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/dialog/z.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/base/ui/widget/CJPayRoundRelativeLayout$Mode.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bdpay/bindcard/lynx/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bdpay/outer/authorize/ui/wrapper/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bdpay/paymentmethod/std/ui/StdPaymentMethodActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/applog/CJPayAgreementDialogLogger$AgreementSource.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/pay/CJPayNewCardActivity$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/ui/BankCardListFragment$CardListAnimationStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/ui/BankCardListFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/ui/CJPayVerificationCodeFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/ui/CJPayVerificationCodeFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/ui/SetPwdActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/bindcard/base/ui/VerifyPwdSafeFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/facelive/core/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/facelive/utils/CJPayFaceEventCenter.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/facelive/utils/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/facelive/utils/q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/facelive/view/CJPayFaceGuideActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/facelive/view/panel/CJPayFaceResultFullPanel.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/fastpay/activity/FastPayActivity$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/activity/IntegratedCounterActivity$v.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/activity/IntegratedCounterActivity$w.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/component/PayComponent.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/component/e$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/component/logger/PayComponentLogger$ShowType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/component/view/ButtonName.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/fragment/CJPayCombineFragment$initViews$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/fragment/SignAndPayFragment$initActions$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/fragment/SignAndPayFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/fragment/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/wrapper/MethodDyPayStdWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/wrapper/MethodDyPayWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/dypay/wrapper/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayConfirmFragment$h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayIndependentCompleteFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/CJPayMethodFragment$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/fragment/q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/game/wrapper/ConfirmGWrapper$initActions$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/utils/a$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/wrapper/BaseConfirmWrapper$SelectPayTypeEnum.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/wrapper/CompleteFullScreenNormalWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/counter/wrapper/CompleteHalfScreenNormalWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/sign/counter/activity/scene/presign/SignPreRouteExecutor.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/sign/counter/fragment/SignConfirmFragment$setButton$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/integrated/sign/counter/fragment/SignConfirmFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/largeamount/ui/CJPayLargeAmountActivity$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRBankCardActivity$f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRBankCardActivity$i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRBankCardActivity$j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRBankCardActivity$k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRBaseActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRIDCardActivity$l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRIdentityActivity$f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRIdentityActivity$i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRIdentityActivity$j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCRIdentityActivity$k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/activity/CJPayOCROptionActivityV2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/data/CJOCRSettingsConfig.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/presenter/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/ocr/wrapper/CJOCRCreditCertWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/superpay/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/superpay/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/superpay/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/activity/CJPayLimitErrorActivity$initAction$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/activity/CJPayLimitErrorActivity$initAction$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/activity/CJPayCheckoutCounterActivity$a0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayAmountUpgradeGuideFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayBdPayContinuePayMethodFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayBioAuthFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayConfirmFragment$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayConfirmFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayMethodFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/CJPayResetPwdGuideFragment$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/fragment/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/result/fragment/CJPayCompleteFragment$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/result/fragment/CJPayMaskFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/counter/utils/CJPayCheckoutCounterProvider.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/CJPayFingerOpenAndPayDialog$onCreate$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/CJPayFingerOpenAndPayDialog$onCreate$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/CJPayFingerprintPresenter.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/CJPayFingerprintService.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/biopromt/CJBioFingerHelper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/n$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/n$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/fingerprint/q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/DyPayUtils.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/dialog/CJPayDoubleConfirmDialog$initView$4$3$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/process/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/process/n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/result/PayResultFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/view/CJPayVerifyPayTypeLayout.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/dypay/wrapper/DyPayCoreWrapper$payNewCardCallBack$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/fragment/CJUnifyPayBioAuthFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/data/CJUnifyTradeCreateScene.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayDoubleVerifyFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper$getErrorDialogClickListener$errorAction$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper$n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper$onBackPressed$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/CJUnifyPayHomePageWrapper$v.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/UnifyPayHomepageState.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayFrontHomePageUIModule$bindData$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayFrontHomePageUIModule$bindData$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayFrontHomePageUIModule$bindData$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayHomePageUIModule$showStyleOpt$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayXRecTopView$bindServiceDetail$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayXRecTopView$initCheckBox$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/CJUnifyPayXRecTopView.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/c0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/f0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/homepage/view/r.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/CJUnifyHalfMethodDialog$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/CJUnifySelectMethodView.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/k$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/k$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/q.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/view/r.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/method/viewholder/CJUnifyFoldViewHolder.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/CJUnifyPayOperationManager.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/utils/CJUnifyPayXRecRenderHelper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyCommonRecView$bindSubTitle$protocolString$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyCommonRecView$bindSubTitle$protocolString$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyCommonRecView$initAction$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyCommonRecView.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyPayXRecBottomView$bindSubTitle$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyPayXRecBottomView$initAction$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/CJUnifyRecMethodView.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/a$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/a$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/b$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/operation/view/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/model/PreVerifyAction.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/model/UnifyPreVerifyType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/utils/UnifyFingerOpenAndPayDialog$onCreate$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/utils/UnifyFingerOpenAndPayDialog$onCreate$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/utils/UnifyFingerOpenAndPayDialog$onCreate$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/utils/UnifyFingerOpenAndPayDialog.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyCarrierVM$fetchThenExchange$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$authFingerprint$1$onAuthSucceeded$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$authFingerprint$1$onAuthSucceeded$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$handleSuccess$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyOpenFingerprintVM$startVerify$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyPasswordVM$PageType.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyPasswordVM$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/UnifyPreVerifyVoiceVM$showMicrophonePermissionSettingsDialog$settingsDialog$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/base/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/j$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/s.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/vm/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/UnifyPreVerifyPwdWrapper$getLynxKeepDialogEventHandler$5.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/UnifyPreVerifyPwdWrapper$initForgetPwdView$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/preverify/wrapper/f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess$handlePreChargeResp$dialog$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayBindCardProcess$start$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayCreditPayProcess$start$1$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayCreditPayProcess$start$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayCreditPayProcess.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPayIncomePayProcess$goToLynxOpenAccount$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPrePayProcess$bindCardCallback$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/CJUnifyPrePayProcess$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/contract/CJUnifyPayProcessState.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/p.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/q$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/r.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/s.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/t.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/process/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$homePageAction$2$1$onCombineCardChangeClick$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$tryCloseWithKeepDialog$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$tryCloseWithKeepDialog$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/CJStandardManager$tryCloseWithKeepDialog$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJPayStandardResultProcess$k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJStandardPayProcess$doubleCheckProcess$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/CJStandardTradeQueryRespWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/w.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/core/x.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$bindBottomArea$2$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$buildKeepDialogConfig$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$6.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$createContentController$7.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$renderFaceRecommendGuide$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmFragment$wrapBankCardPointSwitchListenerForReport$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmPopHandler$interceptIfNeeded$dialog$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/CJStandardDoubleConfirmPopHandler$interceptIfNeeded$dialog$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/front/doubleconfirm/u.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/BaseStandardHomeFragment$renderPreSignGuide$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/BaseStandardHomeFragment$setNoPwdGuideView$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardCvvContentController$onBind$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardHomeManager.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/CJStandardHomePageWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/home/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/marketing/CJStandardDiscountWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/marketing/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/marketing/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodWrapper$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/CJStandardMethodWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/method/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardButtonInfoDialogHandler.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardKeepDialogController$buildKeepDialogEventHandlers$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardKeepDialogController$buildKeepDialogEventHandlers$9.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$13.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$17.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/standard/support/CJStandardRetainDialogManager$buildEventHandlers$8.smali` | 0 | 0 | 1 | 1 |
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
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$eventHandlers$7.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$eventHandlers$8.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/unifypay/utils/retain/DialogEventHandler$reportAndExitCashier$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/CJUnifyPayAssetInfoUtils.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/FrontCounterProvider$startNewET$1$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/FrontCounterProvider$startNewStandard$1$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/FrontCounterProvider.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/front/counter/utils/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainManager$showRecommendPopup$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainManager$showRecommendPopup$2$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/PayAgainManager$startQueryPayType$1$onSuccess$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/adapter/CreditPayVoucherViewHolder$bindData$1$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/b$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/PayAgainMainFragment$onGetMethodListSuccess$performTask$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMainFragment$onGetMethodListSuccess$performTask$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMainFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/fragment/StdPayAgainMethodFragment$initActions$1.smali` | 0 | 0 | 1 | 1 |
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
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/FrontMethodGroupStyleWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/FrontMethodWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideCreditPayWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideNormalWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainGuideVoucherHalfWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initActions$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/PayAgainMainPanelWrapper$initTitleBar$8.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$initActions$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$initActions$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/payagain/wrapper/StdPayAgainMainPanelWrapper$setUpOldSyleLayout$5.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSAgreementDetailFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSAgreementListFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSSmsReceivedExceptionFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/fragment/CJPaySSUpdateCardInfoFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/supplementarysign/utils/CJPaySupplementarySignProvider.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/CJPayUIUtils.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/CreditPayProcessUtils$appendExtInfo$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/CreditPayProcessUtils$appendExtInfo$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/JumpLynxProcessUtil$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/a$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainDialogFromScene.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$businessDidEnter$reportError$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/utils/retaindialog/CJPayRetainEngine$showRetainDialog$4.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b$d$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/b$h.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/c0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/k.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/l.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/s.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/base/x$e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/CJPayVerifyHelperUtils$BubblePosition.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/utils/i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyAgreementListFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyCvvCheckFragment$a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyCvvCheckFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyFingerPrintPreHalfWindowFragment$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyIdentityFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyMaskFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyOneStepPayFragment.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$f.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$getLynxKeepDialogEventHandler$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$getLynxKeepDialogEventHandler$eventHandlers$3.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/VerifyPasswordFragment$o.smali` | 0 | 0 | 1 | 1 |
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
| `com/android/ttcjpaysdk/thirdparty/verify/view/b0.smali` | 0 | 0 | 1 | 1 |
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
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/e.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/g0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/h0.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/verify/view/wrapper/l.smali` | 0 | 0 | 1 | 1 |
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
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession$doVoiceVerify$bizContentParams$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/VoicePrintSession$startRecording$2.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/a.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/bean/VoicePrintOperation.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/bean/VoicePrintResult$DetailCode.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/c.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/common/VoicePrintTracker$MicroAccessStatus.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/common/VoicePrintTracker.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/AudioHelper$stopRecordInternal$2$5$invoked$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/SAMICoreDeNoise$b.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/g.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/i.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/j.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/m.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/n.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/record/o.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/VoicePrintActivity.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/VoicePrintController.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/thirdparty/voiceprint/ui/e.smali` | 0 | 0 | 1 | 1 |
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
| `com/android/ttcjpaysdk/verify/vm/d.smali` | 0 | 0 | 1 | 1 |
| `com/android/ttcjpaysdk/verify/vm/h.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/FqbasePreloadImageMethod$loadFromLocalPath$1.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/b.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/g.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/bridge/impl/r.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/core/g.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/core/h.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/helper/AnniexPageBroadcastHelper$broadcastReceiver$1$onReceive$1.smali` | 0 | 0 | 1 | 1 |
| `com/awesome/fqhybrid/util/ImageLoader.smali` | 0 | 0 | 1 | 1 |
| `com/by/inflate_lib/inflator/TranlateUtilKt.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/base/service/protocol/media/entity/ImageInfo.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/liveplayer/IGameTTLivePlayer$LiveError.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/liveplayer/IGameTTLivePlayer$Orientation.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/pay/model/WxGamePayParamEntity.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/permission/MglServerPermissionAuthPopupConfig$a.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/share/BdpShareBaseInfo$ShareAppInfo.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/api/share/ShareImCallbackInfo$Companion.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/merge/service/model/BdpLocation.smali` | 0 | 0 | 1 | 1 |
| `com/byted/mgl/minigame/interaction/util/InteractionSdkKt.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/BdAccountSeal.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/domain/RegionType.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/sdk/ProcessResult.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/accountseal/view/BdAccountSealActivity.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/ZDataModel$anyMap$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/ZDataModel$jsonObject$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/ZDataModel.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/common/zaid/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/gip/WindMillDetailFragment$f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/gip/WindMillDetailFragment.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/XOpenMethod.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/a0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/b0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/e0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/g.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/n.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/p.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/r.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/y.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ad/live/component/sif/lynxbridge/z.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/AdModel$NativeSiteAdInfo.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/AdModel$WcMiniAppInfo.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/AdModel.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/banner/DynamicAdData$NativeSiteAdInfo.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/adbase/entity/enums/InteractionType$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/banner/impl/BannerAdRequestImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/banner/request/BannerRequestBase.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/admetaversesdk/inspire/impl/ATInspireOpenerImpl$showInspire$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/base/component/BaseRemoteViewsService.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/base/component/BaseXmFgService.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/bean/WakeUpLog.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/core/AllianceServiceImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/hipc/IpcProxyImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/InstrumentationServiceImpl$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/InstrumentationServiceImpl$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a$c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a0$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/a1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/c0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/f0$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/f0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/g0.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/services/impl/h0.smali` | 0 | 0 | 1 | 1 |
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
| `com/bytedance/alliance/utils/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/alliance/utils/k.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adlp/components/api/utils/AdLpBlankDetector$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adlp/components/api/utils/AdLpBlankDetector.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/adtracker/model/C2STrackEvent.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/bridges/bridge/base/g.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/client/components/settings/AbsAdSettingsManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/preload/sif/SifAdPreloadSessionConfig$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/preload/sif/g.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/preload/util/AdPreloadTrace.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/reward/dynamicad/AbsRewardLynxFragment$d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/reward/dynamicad/AbsRewardLynxFragment.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/bridge/BDARLynxBridgeModuleV2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/constant/ActivityTransitionAnimStyle.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/draw/DrawAdLoadMoreDispatcher$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/jsbridge/openreward/OpenRewardRequest.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/rewarded/jsbridge/openreward/d.smali` | 0 | 0 | 1 | 1 |
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
| `com/bytedance/android/ad/sdk/api/ipc/AdIpcCallResponse.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/advideo/ui/LynxAdVideoUI$$PropsSetter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/d.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/gecko/AdGeckoManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/AdIpcAidlService.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/e.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/f.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/j.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/k.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/ipc/n.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/sdk/impl/settings/SettingsManager.smali` | 0 | 0 | 1 | 1 |
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
| `com/bytedance/android/ad/security/adlp/capabilitys/js/JSEvaluateCapability$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceCapability$c$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceProxy$release$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/capabilitys/resource/WebResourceProxy$webReportJson$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/core/AdLpSecManagerFactory.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/adlp/core/exception/SecManagerCreateErrorException$WebViewCastError.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ad/security/api/adlp/AdLpSecContext$isOrangeSite$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/adderive/toptext/TopTextHelper$getLandVideoBlurBitmap$1$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/adderive/toptext/TopTextHelper$preCalculateCoverColor$2$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/adderive/toptext/render/LandingVideoDecorateComponent$LandingVideoDecorateLynxUI.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/alog/Alog$a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ui/ec/widget/feedback/ECFeedbackEnterView.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/ui/ec/widget/switchbutton/CustomSwitchCompat.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/android/util/IntToBooleanJsonAdapter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/instrumentation/interceptor/AddHeaderInterceptor.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/instrumentation/okhttp3/InterceptorImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/tracing/AutoLaunchTraceHelper.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/tracing/AutoPageTraceHelper.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/agent/v2/instrumentation/FragmentTimeAgent.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/config/h.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/entity/ApiAllLocalLog.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/entity/BatteryLogEntity.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/h.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/internal/ApmDelegate$h.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/internal/ApmDelegate$n.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/report/FileUploadServiceImpl.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/trace/fps/FpsTracer$c.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/trace/fps/RealFpsTracer$b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/FpsUtil.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/JsonUtils$JsonWriter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/Pair.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm/util/TimeUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/consumer/slardar/send/DropDataMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/consumer/slardar/send/a.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/consumer/slardar/send/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/apm6/java_alloc/JavaAllocCollector.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/isolate/DataIsolateKey.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/map/api/MapSignalSource.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/monitor/MonitorState.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/PriorityWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackLaunch$3.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackLaunch$inserted$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackTerminate$3.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/AppSession$trackTerminate$inserted$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/CommonKt.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/Engine.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/EventDatabase.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/Model$EventType.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/SessionDatabase.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/i.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/p.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/s.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/applog/priority/original/t.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/article/common/impression/ImpressionManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/TMProcessKillerConfigCache$Companion$repo$2.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/AutoStartObserver$recordFirstStartComponent$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/AutoStartReporter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemscan/ProcessInfoPersist.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/ServiceRedirectV2$tryRedirect$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/ServiceStickSwap$reportAppLog$1.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdauditsdkbase/core/problemsolve/b.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/util/DeviceCategory.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/bdinstall/util/UIUtils.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ies/sdk/widgets/DataCenter.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ies/sdk/widgets/perf/WidgetPerfManager.smali` | 0 | 0 | 1 | 1 |
| `com/bytedance/ies/sdk/widgets/priority/GroupSchedule$1.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$IWXOneJumpAdApi.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$d.smali` | 0 | 0 | 1 | 1 |
| `com/dragon/read/ad/util/WeChatOneJumpUtil$e.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/AbsBaseLoginFragment$j.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$b.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$c.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$d.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/RecallLoginFragment$e.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/component/biz/impl/mine/loginv2/view/CaptchaViewV2$a.smali` | 1 | 0 | 0 | 1 |
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
| `com/dragon/read/util/KeyBoardHelper$OnKeyBoardListener.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/LoadImageCallback.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/PictureUtils$k.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/ToastUtils$l.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/UiConfigSetter$d.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/UiConfigSetter$e.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/UiConfigSetter$m.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/b8$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/c7.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/f$c.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/g2.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/h3$a.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/i2.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/j5.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/k2.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/w1.smali` | 1 | 0 | 0 | 1 |
| `com/dragon/read/util/z9$a.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/account/adapter/InternalAccountAdapter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/android/account/model2/BDAccountPlatformEntity.smali` | 0 | 0 | 1 | 1 |
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
| `com/ss/videoarch/live/LiveIOWrapper$4.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/LiveIOWrapper$LiveIOFunctionCalledByStrategyEngine.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/LiveIOWrapper$LiveIOHandler.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/ttquic/PreloadManager$1.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/ttquic/TTEngineParam.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/live/ttquic/TTLogManager.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/LiveConfigKey.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/MyInvocationHandler.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VLDNSParserImpl.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$25.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$DNSParseCallBack.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$MyErrorListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$MyRetryListener.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/VideoLiveManager$RtcNetworkFilter.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/function/AdaptiveGrading.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/function/SEIReportMgr.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/liveio/LiveIO.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/log/LineSwitcherOnRenderStall.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/log/LogBundle.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/medialoader/MediaLoaderWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/model/LiveInfoSource.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/network/DnsHelper$3.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/network/NetUtils.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/retry/RetryProcessor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/utils/LiveUtils.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer/utils/URLBuilder.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayer.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerAudioLoudnessInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerExtraRenderParams.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerResolution.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerStreamInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerVideoArea.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/liveplayer2/VeLivePlayerVideoStreamInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/nliveplayer/utils/AudioDeviceMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/FeatureBundleBridge.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/LiveStrategyManager$11.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/dataCenter/config/model/PersistenceConfigInfo.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/dataCenter/strategyData/model/NodeCacheInfos.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/featureCenter/featureType/TypeNetworkFeaturesCollector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/featureCenter/featureType/TypePlayFeaturesCollector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/featureCenter/featureType/TypeUserProfileCollector.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/network/LSSDKConfig$DefaultHttpExecutor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/network/NetworkMonitor.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/network/VeLSNetworkManagerImpl.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/strategy/mpdPreload/MpdPreloadManager.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/strategy/networkStrategy/NetworkProber.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/strategy/nodeOptimizer/DnsOptimizer$8.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/strategy/smartStrategy/SuperResolutionStrategy.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/strategy/smartStrategy/TopNHostStrategy.smali` | 0 | 0 | 1 | 1 |
| `com/ss/videoarch/strategy/utils/smartStrategy/PitayaWrapper.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/UnionInfo.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/UserInfo.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/a.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/auth/QQToken.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/auth/a$b.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/auth/a$d.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/auth/c.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/avatar/ImageActivity$QQAvatarImp.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/common/AssistActivity$QQStayReceiver.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/common/AssistActivity.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/common/Constants.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/commonchannel/CommonChannelApi.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/emotion/QQEmotion.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/share/QQShare$1.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/share/QzonePublish$1.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/connect/share/QzonePublish$2.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/channel/a/a.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/diffdev/a/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/diffdev/a/c.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXChannelOpenEvent$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXChannelOpenProfile$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXChannelShareVideo$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXInvoiceAuthInsert$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXLaunchMiniProgram$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXLaunchMiniProgramWithToken$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXNontaxPay$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXPayInsurance$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelbiz/WXPreloadMiniProgram$Req.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelmsg/WXDynamicVideoMiniProgramObject.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelmsg/WXLiteAppObject.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/modelmsg/WXMiniProgramObject.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/mm/opensdk/openapi/MMSharedPreferences$REditor.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/SocialOperation$1.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/SocialOperation$2.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/SocialOperation$3.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/SocialOperation.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/TDialog$FbWebViewClient.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/TDialog$OnTimeListener.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/TDialog.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/b$b.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/b/c.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/b/d.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/b/h$2.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/d$a.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/d$c.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/d.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/im/IM.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/log/SLog.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/miniapp/MiniApp.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/utils/HttpUtils.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/utils/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/utils/i$1.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/utils/i.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/open/utils/k.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/android/dex/Dex.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/android/dex/TableOfContents$Section.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/android/dex/TableOfContents.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/android/utils/SparseBoolArray.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/android/utils/SparseIntArray.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/commons/dexpatcher/struct/PatchOperation.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/MuteLog$2.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/MuteLog.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/MuteLogProxy.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/MuteMaxLoader.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/am/PatchActivityManagerProvider$PluginAMBinder.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/am/PatchActivityManagerProvider.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/dexopt/DexOptimize$2.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/hidden/SystemSupportExt.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/hook/ActivityManagerProxy$StartActivity.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/hook/ActivityManagerProxy.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/hook/ContentProviderProxy.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/signature/ZipUtils.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/utils/FileUtils.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/utils/SharePatchInfo.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/lib/utils/Utils.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/loader/utils/ShareTinkerLog$2.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/loader/utils/ShareTinkerLog.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/ziputils/ziputil/AlignedZipOutputStream.smali` | 0 | 0 | 1 | 1 |
| `com/tencent/tinker/ziputils/ziputil/TinkerZipEntry.smali` | 0 | 0 | 1 | 1 |
| `com/tiktok/ttm/TTMCore.smali` | 0 | 0 | 1 | 1 |
| `com/tokenizer/Tokenizer.smali` | 0 | 0 | 1 | 1 |
| `com/tt/android/qualitystat/a.smali` | 0 | 0 | 1 | 1 |
| `com/tt/android/qualitystat/base/b.smali` | 0 | 0 | 1 | 1 |
| `com/tt/android/qualitystat/config/b$a.smali` | 0 | 0 | 1 | 1 |
| `com/tt/android/qualitystat/duration/d.smali` | 0 | 0 | 1 | 1 |
| `com/tt/miniapphost/entity/OatVerifyEntity.smali` | 0 | 0 | 1 | 1 |
| `com/ttnet/org/chromium/base/j.smali` | 0 | 0 | 1 | 1 |
| `com/ttnet/org/chromium/net/NetStringUtil.smali` | 0 | 0 | 1 | 1 |
| `com/ttnet/org/chromium/net/impl/CronetFrontierClient.smali` | 0 | 0 | 1 | 1 |
| `com/ttnet/org/chromium/net/urlconnection/g.smali` | 0 | 0 | 1 | 1 |
| `com/ttreader/ttepubparser/TTEPubParser.smali` | 0 | 0 | 1 | 1 |
| `com/ttreader/tthtmlparser/parser/TTHtmlManager.smali` | 0 | 0 | 1 | 1 |
| `com/ttreader/tttext/FontCache.smali` | 0 | 0 | 1 | 1 |
| `com/ttreader/tttext/TTTextLayout.smali` | 0 | 0 | 1 | 1 |
| `com/ttreader/tttext/g.smali` | 0 | 0 | 1 | 1 |
| `com/ttreader/tttext/l.smali` | 0 | 0 | 1 | 1 |
| `com/unionpay/WebViewJavascriptBridge.smali` | 0 | 0 | 1 | 1 |
| `com/unionpay/b.smali` | 0 | 0 | 1 | 1 |
| `com/unionpay/o.smali` | 0 | 0 | 1 | 1 |
| `com/unionpay/q.smali` | 0 | 0 | 1 | 1 |
| `com/unionpay/utils/a.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/VivoPushMessageReceiver.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/b/m.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/b/p.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/c/a.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/d/b.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/g/c.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/aa.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/ab.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/ac.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/ao.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/d.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/e.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/y.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/h/z.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/k.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/model/UnvarnishedMessage.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/model/a.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/t.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/util/NotifyUtil.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/util/a.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/util/ae.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/util/al.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/util/k.smali` | 0 | 0 | 1 | 1 |
| `com/vivo/push/util/n.smali` | 0 | 0 | 1 | 1 |
| `d40/a.smali` | 0 | 0 | 1 | 1 |
| `d60/a.smali` | 0 | 0 | 1 | 1 |
| `dd/c$a.smali` | 0 | 0 | 1 | 1 |
| `dd/c.smali` | 0 | 0 | 1 | 1 |
| `di/b.smali` | 0 | 0 | 1 | 1 |
| `di/d.smali` | 0 | 0 | 1 | 1 |
| `dl/a.smali` | 0 | 0 | 1 | 1 |
| `dl/a0.smali` | 0 | 0 | 1 | 1 |
| `dl/b.smali` | 0 | 0 | 1 | 1 |
| `dl/c.smali` | 0 | 0 | 1 | 1 |
| `dl/c0.smali` | 0 | 0 | 1 | 1 |
| `dl/h0.smali` | 0 | 0 | 1 | 1 |
| `dl/j.smali` | 0 | 0 | 1 | 1 |
| `dl/k.smali` | 0 | 0 | 1 | 1 |
| `dl/l.smali` | 0 | 0 | 1 | 1 |
| `dl/m.smali` | 0 | 0 | 1 | 1 |
| `dl/q.smali` | 0 | 0 | 1 | 1 |
| `dl/s.smali` | 0 | 0 | 1 | 1 |
| `dl/t.smali` | 0 | 0 | 1 | 1 |
| `dl/u.smali` | 0 | 0 | 1 | 1 |
| `dl/v.smali` | 0 | 0 | 1 | 1 |
| `dl/y.smali` | 0 | 0 | 1 | 1 |
| `dl/z.smali` | 0 | 0 | 1 | 1 |
| `dn/b.smali` | 0 | 0 | 1 | 1 |
| `do/e$b.smali` | 0 | 0 | 1 | 1 |
| `do/e.smali` | 0 | 0 | 1 | 1 |
| `do/f.smali` | 0 | 0 | 1 | 1 |
| `e20/a.smali` | 0 | 0 | 1 | 1 |
| `e60/a.smali` | 0 | 0 | 1 | 1 |
| `e70/e.smali` | 0 | 0 | 1 | 1 |
| `e70/k.smali` | 0 | 0 | 1 | 1 |
| `e70/m.smali` | 0 | 0 | 1 | 1 |
| `e8/c$b.smali` | 0 | 0 | 1 | 1 |
| `e8/c$c.smali` | 0 | 0 | 1 | 1 |
| `e8/d.smali` | 0 | 0 | 1 | 1 |
| `ea/b.smali` | 0 | 0 | 1 | 1 |
| `eb/f.smali` | 0 | 0 | 1 | 1 |
| `eh/a.smali` | 0 | 0 | 1 | 1 |
| `eh/b.smali` | 0 | 0 | 1 | 1 |
| `eh/c.smali` | 0 | 0 | 1 | 1 |
| `eh/g.smali` | 0 | 0 | 1 | 1 |
| `eh/h.smali` | 0 | 0 | 1 | 1 |
| `eh/i.smali` | 0 | 0 | 1 | 1 |
| `eh/j.smali` | 0 | 0 | 1 | 1 |
| `eh/o.smali` | 0 | 0 | 1 | 1 |
| `el/b$a.smali` | 0 | 0 | 1 | 1 |
| `el/b.smali` | 0 | 0 | 1 | 1 |
| `el/d.smali` | 0 | 0 | 1 | 1 |
| `er/c.smali` | 0 | 0 | 1 | 1 |
| `fb/b.smali` | 0 | 0 | 1 | 1 |
| `fb/c.smali` | 0 | 0 | 1 | 1 |
| `fb/f.smali` | 0 | 0 | 1 | 1 |
| `fb/h.smali` | 0 | 0 | 1 | 1 |
| `fk/d.smali` | 0 | 0 | 1 | 1 |
| `fo/g.smali` | 0 | 0 | 1 | 1 |
| `g40/e.smali` | 0 | 0 | 1 | 1 |
| `g50/a.smali` | 0 | 0 | 1 | 1 |
| `g8/h$a.smali` | 0 | 0 | 1 | 1 |
| `g8/i.smali` | 0 | 0 | 1 | 1 |
| `g8/j.smali` | 0 | 0 | 1 | 1 |
| `g9/e.smali` | 0 | 0 | 1 | 1 |
| `gb/a.smali` | 0 | 0 | 1 | 1 |
| `gc/b.smali` | 0 | 0 | 1 | 1 |
| `gg/h.smali` | 0 | 0 | 1 | 1 |
| `gg/i.smali` | 0 | 0 | 1 | 1 |
| `gh/a.smali` | 0 | 0 | 1 | 1 |
| `gk/a.smali` | 0 | 0 | 1 | 1 |
| `gm/e.smali` | 0 | 0 | 1 | 1 |
| `h40/d.smali` | 0 | 0 | 1 | 1 |
| `hc/a.smali` | 0 | 0 | 1 | 1 |
| `hh/b.smali` | 0 | 0 | 1 | 1 |
| `hh/g.smali` | 0 | 0 | 1 | 1 |
| `hi/a.smali` | 0 | 0 | 1 | 1 |
| `hi/b.smali` | 0 | 0 | 1 | 1 |
| `hl/a.smali` | 0 | 0 | 1 | 1 |
| `hl/b.smali` | 0 | 0 | 1 | 1 |
| `hn/d.smali` | 0 | 0 | 1 | 1 |
| `i40/f.smali` | 0 | 0 | 1 | 1 |
| `i60/a.smali` | 0 | 0 | 1 | 1 |
| `ia/d.smali` | 0 | 0 | 1 | 1 |
| `ia/e.smali` | 0 | 0 | 1 | 1 |
| `ia/f.smali` | 0 | 0 | 1 | 1 |
| `ia/h.smali` | 0 | 0 | 1 | 1 |
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
| `il/b.smali` | 0 | 0 | 1 | 1 |
| `in/d.smali` | 0 | 0 | 1 | 1 |
| `jb/b.smali` | 0 | 0 | 1 | 1 |
| `jb/d.smali` | 0 | 0 | 1 | 1 |
| `jb/e.smali` | 0 | 0 | 1 | 1 |
| `jb/l.smali` | 0 | 0 | 1 | 1 |
| `jb/t.smali` | 0 | 0 | 1 | 1 |
| `jb/v.smali` | 0 | 0 | 1 | 1 |
| `jg/a$a.smali` | 0 | 0 | 1 | 1 |
| `jk/b.smali` | 0 | 0 | 1 | 1 |
| `jo/a$b.smali` | 0 | 0 | 1 | 1 |
| `k40/c.smali` | 0 | 0 | 1 | 1 |
| `k40/d.smali` | 0 | 0 | 1 | 1 |
| `k80/d.smali` | 0 | 0 | 1 | 1 |
| `k80/f.smali` | 0 | 0 | 1 | 1 |
| `ka/d.smali` | 0 | 0 | 1 | 1 |
| `kc/e.smali` | 0 | 0 | 1 | 1 |
| `ke/d.smali` | 0 | 0 | 1 | 1 |
| `kn/e.smali` | 0 | 0 | 1 | 1 |
| `kn/h.smali` | 0 | 0 | 1 | 1 |
| `l40/c.smali` | 0 | 0 | 1 | 1 |
| `l60/a.smali` | 0 | 0 | 1 | 1 |
| `l80/a$a.smali` | 0 | 0 | 1 | 1 |
| `l80/a.smali` | 0 | 0 | 1 | 1 |
| `l80/r$c.smali` | 0 | 0 | 1 | 1 |
| `l80/r.smali` | 0 | 0 | 1 | 1 |
| `la/b.smali` | 0 | 0 | 1 | 1 |
| `la/c.smali` | 0 | 0 | 1 | 1 |
| `lb/d.smali` | 0 | 0 | 1 | 1 |
| `lb/e.smali` | 0 | 0 | 1 | 1 |
| `lc/l.smali` | 0 | 0 | 1 | 1 |
| `lc/u$a.smali` | 0 | 0 | 1 | 1 |
| `lc/y.smali` | 0 | 0 | 1 | 1 |
| `li/a.smali` | 0 | 0 | 1 | 1 |
| `ll/a$b.smali` | 0 | 0 | 1 | 1 |
| `ll/b.smali` | 0 | 0 | 1 | 1 |
| `lq/a$a.smali` | 0 | 0 | 1 | 1 |
| `m20/a.smali` | 0 | 0 | 1 | 1 |
| `m60/c.smali` | 0 | 0 | 1 | 1 |
| `m60/k$a.smali` | 0 | 0 | 1 | 1 |
| `m60/m.smali` | 0 | 0 | 1 | 1 |
| `ma/a.smali` | 0 | 0 | 1 | 1 |
| `ma/b.smali` | 0 | 0 | 1 | 1 |
| `mb/a.smali` | 0 | 0 | 1 | 1 |
| `mb/f.smali` | 0 | 0 | 1 | 1 |
| `mb/m.smali` | 0 | 0 | 1 | 1 |
| `mb/w.smali` | 0 | 0 | 1 | 1 |
| `mb/x.smali` | 0 | 0 | 1 | 1 |
| `mf/c.smali` | 0 | 0 | 1 | 1 |
| `mk/a$a$a.smali` | 0 | 0 | 1 | 1 |
| `mn/c.smali` | 0 | 0 | 1 | 1 |
| `mq/a$a.smali` | 0 | 0 | 1 | 1 |
| `n20/f.smali` | 0 | 0 | 1 | 1 |
| `n20/g.smali` | 0 | 0 | 1 | 1 |
| `n30/b.smali` | 0 | 0 | 1 | 1 |
| `n30/c.smali` | 0 | 0 | 1 | 1 |
| `n30/f.smali` | 0 | 0 | 1 | 1 |
| `n30/g.smali` | 0 | 0 | 1 | 1 |
| `n60/b$a.smali` | 0 | 0 | 1 | 1 |
| `n60/b.smali` | 0 | 0 | 1 | 1 |
| `n9/a.smali` | 0 | 0 | 1 | 1 |
| `na/a.smali` | 0 | 0 | 1 | 1 |
| `nc/a.smali` | 0 | 0 | 1 | 1 |
| `nd/f.smali` | 0 | 0 | 1 | 1 |
| `nd/i.smali` | 0 | 0 | 1 | 1 |
| `nf/a.smali` | 0 | 0 | 1 | 1 |
| `nk/a$b$a$a.smali` | 0 | 0 | 1 | 1 |
| `nk/b.smali` | 0 | 0 | 1 | 1 |
| `nk/c.smali` | 0 | 0 | 1 | 1 |
| `nk/d.smali` | 0 | 0 | 1 | 1 |
| `np/a.smali` | 0 | 0 | 1 | 1 |
| `np/b.smali` | 0 | 0 | 1 | 1 |
| `nq/a.smali` | 0 | 0 | 1 | 1 |
| `o40/b.smali` | 0 | 0 | 1 | 1 |
| `od/k.smali` | 0 | 0 | 1 | 1 |
| `oe/e$a.smali` | 0 | 0 | 1 | 1 |
| `oe/f.smali` | 0 | 0 | 1 | 1 |
| `og/a.smali` | 0 | 0 | 1 | 1 |
| `oi/d.smali` | 0 | 0 | 1 | 1 |
| `ok/a.smali` | 0 | 0 | 1 | 1 |
| `ol/b.smali` | 0 | 0 | 1 | 1 |
| `p8/a$a.smali` | 0 | 0 | 1 | 1 |
| `p8/a.smali` | 0 | 0 | 1 | 1 |
| `p8/e.smali` | 0 | 0 | 1 | 1 |
| `p8/g.smali` | 0 | 0 | 1 | 1 |
| `p8/i.smali` | 0 | 0 | 1 | 1 |
| `p8/j.smali` | 0 | 0 | 1 | 1 |
| `p8/n.smali` | 0 | 0 | 1 | 1 |
| `p8/q$a.smali` | 0 | 0 | 1 | 1 |
| `p8/q.smali` | 0 | 0 | 1 | 1 |
| `pk/f$a.smali` | 0 | 0 | 1 | 1 |
| `pk/g.smali` | 0 | 0 | 1 | 1 |
| `pl/a.smali` | 0 | 0 | 1 | 1 |
| `pm/b.smali` | 0 | 0 | 1 | 1 |
| `pp/c.smali` | 0 | 0 | 1 | 1 |
| `q30/h.smali` | 0 | 0 | 1 | 1 |
| `q30/j.smali` | 0 | 0 | 1 | 1 |
| `q40/a.smali` | 0 | 0 | 1 | 1 |
| `qb/a.smali` | 0 | 0 | 1 | 1 |
| `qe/b.smali` | 0 | 0 | 1 | 1 |
| `qe/c$a.smali` | 0 | 0 | 1 | 1 |
| `qf/e.smali` | 0 | 0 | 1 | 1 |
| `qg/f.smali` | 0 | 0 | 1 | 1 |
| `qi/a.smali` | 0 | 0 | 1 | 1 |
| `qi/b.smali` | 0 | 0 | 1 | 1 |
| `qi/d$e$b.smali` | 0 | 0 | 1 | 1 |
| `qn/c.smali` | 0 | 0 | 1 | 1 |
| `qq/h.smali` | 0 | 0 | 1 | 1 |
| `rb/c.smali` | 0 | 0 | 1 | 1 |
| `rd/b.smali` | 0 | 0 | 1 | 1 |
| `ri/c$a.smali` | 0 | 0 | 1 | 1 |
| `rl/a.smali` | 0 | 0 | 1 | 1 |
| `rl/b.smali` | 0 | 0 | 1 | 1 |
| `s20/b.smali` | 0 | 0 | 1 | 1 |
| `s40/b.smali` | 0 | 0 | 1 | 1 |
| `s70/d.smali` | 0 | 0 | 1 | 1 |
| `sa3/a.smali` | 0 | 0 | 1 | 1 |
| `sb/c.smali` | 0 | 0 | 1 | 1 |
| `sb/d.smali` | 0 | 0 | 1 | 1 |
| `sc/a$e.smali` | 0 | 0 | 1 | 1 |
| `sc/a.smali` | 0 | 0 | 1 | 1 |
| `sc/b.smali` | 0 | 0 | 1 | 1 |
| `sf/a$a.smali` | 0 | 0 | 1 | 1 |
| `sj/d.smali` | 0 | 0 | 1 | 1 |
| `sj/g.smali` | 0 | 0 | 1 | 1 |
| `t20/d.smali` | 0 | 0 | 1 | 1 |
| `t20/h.smali` | 0 | 0 | 1 | 1 |
| `t20/j.smali` | 0 | 0 | 1 | 1 |
| `t30/e.smali` | 0 | 0 | 1 | 1 |
| `t30/f.smali` | 0 | 0 | 1 | 1 |
| `t60/e.smali` | 0 | 0 | 1 | 1 |
| `t60/f.smali` | 0 | 0 | 1 | 1 |
| `t60/g.smali` | 0 | 0 | 1 | 1 |
| `tb/a.smali` | 0 | 0 | 1 | 1 |
| `tf/c.smali` | 0 | 0 | 1 | 1 |
| `tg/a.smali` | 0 | 0 | 1 | 1 |
| `tg/b.smali` | 0 | 0 | 1 | 1 |
| `tg/c.smali` | 0 | 0 | 1 | 1 |
| `tg/f.smali` | 0 | 0 | 1 | 1 |
| `tg/j.smali` | 0 | 0 | 1 | 1 |
| `tg/n.smali` | 0 | 0 | 1 | 1 |
| `tg/o.smali` | 0 | 0 | 1 | 1 |
| `ti/a.smali` | 0 | 0 | 1 | 1 |
| `tj/i.smali` | 0 | 0 | 1 | 1 |
| `tj/j.smali` | 0 | 0 | 1 | 1 |
| `tp/a.smali` | 0 | 0 | 1 | 1 |
| `u20/a.smali` | 0 | 0 | 1 | 1 |
| `u20/c.smali` | 0 | 0 | 1 | 1 |
| `u20/d.smali` | 0 | 0 | 1 | 1 |
| `u60/c.smali` | 0 | 0 | 1 | 1 |
| `u60/d$a.smali` | 0 | 0 | 1 | 1 |
| `u9/a$a.smali` | 0 | 0 | 1 | 1 |
| `u9/b$a.smali` | 0 | 0 | 1 | 1 |
| `ua/b.smali` | 0 | 0 | 1 | 1 |
| `ui/b.smali` | 0 | 0 | 1 | 1 |
| `ui/c.smali` | 0 | 0 | 1 | 1 |
| `uj/a.smali` | 0 | 0 | 1 | 1 |
| `uj/d.smali` | 0 | 0 | 1 | 1 |
| `v40/a.smali` | 0 | 0 | 1 | 1 |
| `v9/a.smali` | 0 | 0 | 1 | 1 |
| `vb/f$a.smali` | 0 | 0 | 1 | 1 |
| `vc/a.smali` | 0 | 0 | 1 | 1 |
| `vc/b.smali` | 0 | 0 | 1 | 1 |
| `vf/a.smali` | 0 | 0 | 1 | 1 |
| `vf/f.smali` | 0 | 0 | 1 | 1 |
| `w20/e$b.smali` | 0 | 0 | 1 | 1 |
| `w20/e.smali` | 0 | 0 | 1 | 1 |
| `w20/m.smali` | 0 | 0 | 1 | 1 |
| `w30/a.smali` | 0 | 0 | 1 | 1 |
| `w40/a$a.smali` | 0 | 0 | 1 | 1 |
| `w50/c.smali` | 0 | 0 | 1 | 1 |
| `wd/b$e.smali` | 0 | 0 | 1 | 1 |
| `wd/b.smali` | 0 | 0 | 1 | 1 |
| `wj/b$a.smali` | 0 | 0 | 1 | 1 |
| `wj/b$d.smali` | 0 | 0 | 1 | 1 |
| `wj/b$e.smali` | 0 | 0 | 1 | 1 |
| `wq/a.smali` | 0 | 0 | 1 | 1 |
| `wr2/e.smali` | 0 | 0 | 1 | 1 |
| `wr2/g.smali` | 0 | 0 | 1 | 1 |
| `wr2/k.smali` | 0 | 0 | 1 | 1 |
| `wr2/m.smali` | 0 | 0 | 1 | 1 |
| `wr2/o.smali` | 0 | 0 | 1 | 1 |
| `wr2/s.smali` | 0 | 0 | 1 | 1 |
| `ws2/b.smali` | 0 | 0 | 1 | 1 |
| `ws2/c.smali` | 0 | 0 | 1 | 1 |
| `wv2/g$a.smali` | 0 | 0 | 1 | 1 |
| `wz2/a.smali` | 0 | 0 | 1 | 1 |
| `wz2/c.smali` | 0 | 0 | 1 | 1 |
| `wz2/d.smali` | 0 | 0 | 1 | 1 |
| `wz2/f.smali` | 0 | 0 | 1 | 1 |
| `wz2/k.smali` | 0 | 0 | 1 | 1 |
| `wz2/l$b$a.smali` | 0 | 0 | 1 | 1 |
| `wz2/l$b$b.smali` | 0 | 0 | 1 | 1 |
| `wz2/l$b.smali` | 0 | 0 | 1 | 1 |
| `x50/b.smali` | 0 | 0 | 1 | 1 |
| `x63/a.smali` | 0 | 0 | 1 | 1 |
| `xa/a.smali` | 0 | 0 | 1 | 1 |
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
| `xf/e.smali` | 0 | 0 | 1 | 1 |
| `xf/h$a.smali` | 0 | 0 | 1 | 1 |
| `xf/h.smali` | 0 | 0 | 1 | 1 |
| `xf/i.smali` | 0 | 0 | 1 | 1 |
| `xh/h.smali` | 0 | 0 | 1 | 1 |
| `xj/a.smali` | 0 | 0 | 1 | 1 |
| `xm2/a$a.smali` | 0 | 0 | 1 | 1 |
| `xo2/d.smali` | 0 | 0 | 1 | 1 |
| `xo2/g.smali` | 0 | 0 | 1 | 1 |
| `xu2/d.smali` | 0 | 0 | 1 | 1 |
| `xx2/a.smali` | 0 | 0 | 1 | 1 |
| `xx2/c.smali` | 0 | 0 | 1 | 1 |
| `y13/a.smali` | 0 | 0 | 1 | 1 |
| `y43/a.smali` | 0 | 0 | 1 | 1 |
| `y73/a.smali` | 0 | 0 | 1 | 1 |
| `yb/c.smali` | 0 | 0 | 1 | 1 |
| `ye/a.smali` | 0 | 0 | 1 | 1 |
| `ye/d.smali` | 0 | 0 | 1 | 1 |
| `yf/e.smali` | 0 | 0 | 1 | 1 |
| `yj2/b.smali` | 0 | 0 | 1 | 1 |
| `ym2/t.smali` | 0 | 0 | 1 | 1 |
| `yn/a.smali` | 0 | 0 | 1 | 1 |
| `yo2/d.smali` | 0 | 0 | 1 | 1 |
| `yo7/d.smali` | 0 | 0 | 1 | 1 |
| `yo7/l$a.smali` | 0 | 0 | 1 | 1 |
| `yu2/b.smali` | 0 | 0 | 1 | 1 |
| `yw2/d.smali` | 0 | 0 | 1 | 1 |
| `yx2/a.smali` | 0 | 0 | 1 | 1 |
| `yx2/s.smali` | 0 | 0 | 1 | 1 |
| `yy2/b.smali` | 0 | 0 | 1 | 1 |
| `yy2/v.smali` | 0 | 0 | 1 | 1 |
| `z13/b.smali` | 0 | 0 | 1 | 1 |
| `z23/f$d.smali` | 0 | 0 | 1 | 1 |
| `z33/c1.smali` | 0 | 0 | 1 | 1 |
| `z33/f1.smali` | 0 | 0 | 1 | 1 |
| `z33/i0.smali` | 0 | 0 | 1 | 1 |
| `z33/l.smali` | 0 | 0 | 1 | 1 |
| `z33/s.smali` | 0 | 0 | 1 | 1 |
| `z33/v.smali` | 0 | 0 | 1 | 1 |
| `z33/w0.smali` | 0 | 0 | 1 | 1 |
| `z33/x.smali` | 0 | 0 | 1 | 1 |
| `z33/z0.smali` | 0 | 0 | 1 | 1 |
| `z40/a$b$a.smali` | 0 | 0 | 1 | 1 |
| `z43/c.smali` | 0 | 0 | 1 | 1 |
| `z43/g.smali` | 0 | 0 | 1 | 1 |
| `z43/p.smali` | 0 | 0 | 1 | 1 |
| `z60/a$b.smali` | 0 | 0 | 1 | 1 |
| `z60/b.smali` | 0 | 0 | 1 | 1 |
| `z60/c.smali` | 0 | 0 | 1 | 1 |
| `z73/c.smali` | 0 | 0 | 1 | 1 |
| `z73/d.smali` | 0 | 0 | 1 | 1 |
| `z8/b.smali` | 0 | 0 | 1 | 1 |
| `za/a.smali` | 0 | 0 | 1 | 1 |
| `zb/c.smali` | 0 | 0 | 1 | 1 |
| `zd/c$a.smali` | 0 | 0 | 1 | 1 |
| `zd/e$a.smali` | 0 | 0 | 1 | 1 |
| `zi/c$a.smali` | 0 | 0 | 1 | 1 |
| `zi/c.smali` | 0 | 0 | 1 | 1 |
| `zj2/n.smali` | 0 | 0 | 1 | 1 |
| `zj2/s.smali` | 0 | 0 | 1 | 1 |
| `zk2/d.smali` | 0 | 0 | 1 | 1 |
| `zn/b.smali` | 0 | 0 | 1 | 1 |
| `zn/c.smali` | 0 | 0 | 1 | 1 |
| `zn2/h0.smali` | 0 | 0 | 1 | 1 |
| `zn2/i0.smali` | 0 | 0 | 1 | 1 |
| `zn2/q.smali` | 0 | 0 | 1 | 1 |
| `zu2/h.smali` | 0 | 0 | 1 | 1 |
| `zu2/i.smali` | 0 | 0 | 1 | 1 |
| `zy2/c.smali` | 0 | 0 | 1 | 1 |
| `zy2/i.smali` | 0 | 0 | 1 | 1 |
| `zy2/l0.smali` | 0 | 0 | 1 | 1 |
| `zy2/m.smali` | 0 | 0 | 1 | 1 |
| `zy2/m0.smali` | 0 | 0 | 1 | 1 |
| `zy2/n.smali` | 0 | 0 | 1 | 1 |
| `zy2/u.smali` | 0 | 0 | 1 | 1 |

## 4. 真删除类清单

（无——破解者未删除任何官方类，与番茄 16a 行为一致）

## 5. dex 挪位对照（重打包证据，无语义）

- 同名类在 mod/inner 都出现且来源 dex 不同的数量（挪位规模，信息项）: 类名对齐总数 282632

## 6. 归档结构

```
hg1-diff-baksmali/
├── added/    真新增类 baksmali 全文
├── changed/  修改类差异方法全文（三段标注）
└── removed/  删除类 inner 全文
```

## 7. 与番茄 round16a 壳类画像重合分析

> 口径：主类名归一（`X$a`/`X$1` → `X`），红果真新增类 × 番茄 16a 真新增 1249 类画像。
> 红果真新增 1223 个 .smali 文件 = 归一后 **1213 主类**；画像基线 1249 归一 1213 主类。

### ★ 公共类重合率 = 1123 / 1213 = **92.6%** （≥30%，未触红旗）

### 重合类按包分组（A 类候选：壳代码）

| 包前缀 | 类数 |
|---|---|
| `com/` | 1079 |
| `org/checkerframework/` | 33 |
| `org/lsposed/` | 6 |
| `com/pandora/` | 3 |
| `sgcore0/` | 1 |
| `sgcore0/hidden/` | 1 |

### 红果独有类按包分组（B/C/D 类候选——番茄壳中不存在）

| 包前缀 | 类数 |
|---|---|
| `com/dragon/` | 61 |
| `com/ss/` | 10 |
| `com/pandora/` | 8 |
| `an2/` | 7 |
| `com/` | 3 |
| `com/b/` | 1 |

### 红果独有类完整清单

```
an2/۟۠ۢۥ
an2/ۣ۟ۧۢۤ
an2/۠ۤۦۣ
an2/ۡۨۡۥ
an2/ۣۣۥ۟
an2/ۣۤۡۧ
an2/ۧۨ۟۟
com/b/a
com/dragon/read/ad/util/ۣۤۢ۟
com/dragon/read/base/ssconfig/model/۟۠ۢۢ
com/dragon/read/base/ssconfig/model/۟ۤۦۨۧ
com/dragon/read/base/ssconfig/model/۟ۥۡۨۧ
com/dragon/read/base/ssconfig/model/ۣۡۨۥ
com/dragon/read/base/ssconfig/model/ۣۤۢۦ
com/dragon/read/base/ssconfig/model/ۤۧ۠ۦ
com/dragon/read/base/ssconfig/model/ۥۡۢ۠
com/dragon/read/base/ssconfig/model/ۣۣۧۤ
com/dragon/read/component/biz/impl/mine/card/model/۟ۤۢۡۥ
com/dragon/read/component/biz/impl/mine/card/model/۟ۥۥۣۡ
com/dragon/read/component/biz/impl/mine/card/model/۟ۦۢۨۤ
com/dragon/read/component/biz/impl/mine/card/model/ۣۣ۟ۧ۠
com/dragon/read/component/biz/impl/mine/card/model/ۣ۟ۧۦ۟
com/dragon/read/component/biz/impl/mine/card/model/۟ۧۤۢۤ
com/dragon/read/component/biz/impl/mine/loginv2/view/۟۠ۥۦ۠
com/dragon/read/component/biz/impl/mine/loginv2/view/۟ۦ۠ۦۥ
com/dragon/read/component/biz/impl/mine/loginv2/view/۟ۧۧۥۨ
com/dragon/read/component/biz/impl/mine/loginv2/view/۠ۥۥ
com/dragon/read/component/biz/impl/mine/loginv2/view/ۣۡ۟ۥ
com/dragon/read/component/biz/impl/mine/loginv2/view/ۤۦ۠ۡ
com/dragon/read/component/biz/impl/mine/۟۟ۤۦۡ
com/dragon/read/component/biz/impl/mine/۟ۢۥۣۢ
com/dragon/read/component/biz/impl/mine/ۣ۟ۨۢۧ
com/dragon/read/component/biz/impl/mine/۟ۦ۠ۢ۠
com/dragon/read/component/biz/impl/mine/۟ۧۡۨۡ
com/dragon/read/component/biz/impl/mine/ۣۣ
com/dragon/read/pages/main/۟ۥۣۦۢ
com/dragon/read/pages/main/۟ۥۦۧۥ
com/dragon/read/pages/main/ۨۦۡۡ
com/dragon/read/polaris/۟۟۠ۥ
com/dragon/read/polaris/۟۠ۦۨۢ
com/dragon/read/polaris/۟۠ۧ۠۟
com/dragon/read/polaris/۟ۢ۟ۡ۟
com/dragon/read/polaris/ۣۣ۟۠۟
com/dragon/read/polaris/۟ۤ۟۠ۥ
com/dragon/read/polaris/ۣ۠ۨۨ
com/dragon/read/polaris/ۧۢۨ۟
com/dragon/read/reader/ad/noad/۟۠ۥۤۢ
com/dragon/read/reader/ad/noad/ۢۨۧۧ
com/dragon/read/reader/ad/noad/ۤۥۧ۠
com/dragon/read/reader/ad/۟ۦۣۣۣ
com/dragon/read/reader/ad/ۣ۠ۢۨ
com/dragon/read/reader/ad/ۣۡۨۧ
com/dragon/read/reader/ad/ۢۨ۠ۡ
com/dragon/read/reader/ad/ۤۢۢۤ
com/dragon/read/reader/ad/ۤۥۧ
com/dragon/read/reader/ad/ۦۣۧۢ
com/dragon/read/rpc/rpc/ۣۣ۟۟ۤ
com/dragon/read/rpc/rpc/۟ۡۦ۟ۥ
com/dragon/read/rpc/rpc/ۣ۟ۧ۟ۡ
com/dragon/read/rpc/rpc/۟ۧۦۡۥ
com/dragon/read/rpc/rpc/ۡ۠ۤۧ
com/dragon/read/rpc/rpc/ۣ۠ۤۦ
com/dragon/read/rpc/rpc/ۨۦۤ
com/dragon/read/user/model/۟ۤۧۢ
com/dragon/read/user/model/۟ۥ۟ۦ
com/dragon/read/user/model/۟ۦۣۢۡ
com/dragon/read/user/model/۟ۧۦۣ
com/dragon/read/user/model/ۦۣۣۧ
com/dragon/read/util/ۦۧۥۡ
com/pandora/core/۟ۡۥۨ
com/pandora/core/۟ۢۡ۠ۤ
com/pandora/core/ۣ۟ۦ
com/pandora/core/۟ۤ۠ۨ۠
com/pandora/core/۟ۤۧۢۥ
com/pandora/core/۟ۧۥۦۣ
com/pandora/core/ۡۢۦۤ
com/pandora/core/ۢۧ۠ۥ
com/ss/android/update/۟۟ۤۤۡ
com/ss/android/update/ۣۣ۟ۢۨ
com/ss/android/update/۟ۤۡۡۤ
com/ss/android/update/۟ۤۤۨۥ
com/ss/android/update/۟ۥۧۦۣ
com/ss/android/update/ۣۥۣۣ
com/ss/android/update/ۣۣۨۨ
com/ss/android/update/ۦۥ۠ۡ
com/ss/android/update/ۧ۠ۧۨ
com/ss/android/update/ۣۧ۟ۥ
com/tY
com/tZ
com/ua
```

> 画像独有（番茄有红果无，信息项）: 90 主类
