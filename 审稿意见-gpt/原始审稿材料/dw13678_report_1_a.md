# Report for DW13678 Fang

The authors construct an anomaly-free, renormalizable model in which an additional Abelian gauge field $A^{\prime}$ has chiral couplings to muons and taus. This model realizes a limit where the $A^{\prime}$ coupling to the $\mu$-$\tau$ current is axial. The second goal of the paper is to examine the phenomenology of this model in the axial limit.

The paper presents results that are useful for the model building community. However, I have some significant reservations about key points that either should be included or otherwise justified in being excluded from the manuscript. These are explained below. Revisions for these major points (even if only to clarify why they are not issues) are required before the paper is at the level of a PRD manuscript.

## Merits of the paper

- The model construction section is written clearly. While the key ingredients for constructing such a model already exist in the literature, the authors have put these ingredients together.
- The phenomenology is reasonably well motivated (up to some of the points below) and are straightforward to follow.
- The paper is presented in a way that will make it useful for model builders to implement into their own models.

## Major Points That Must Be Addressed

The following points should be addressed in the paper. In this referee report I make suggestions based on my understanding of the manuscript narrative. If I am mistaken, then perhaps the point of confusion merits clarification in the manuscript.

### 1. Phenomenology of the $S$ scalar

The second half of the paper reviews a set of experimental bounds on only an effective theory of the $A^{\prime}$ axially coupled to the $L_{\mu-\tau}$ current. This leaves a major gap between these two parts of the paper: the authors show that their UV theory requires a scalar $S$ that cannot be arbitrarily decoupled from the low-energy dynamics, e.g. from (34) which states that $m_{S}^{2}<4\pi(m_{A^{\prime}}/2g_{X})^{2}$.

1. It is thus an odd choice to exclude the scalar from the phenomenology of the effective theory: if the $S$ is unavoidable at phenomenologically relevant scales, shouldn't one of the main points of the paper be that the only known UV completion of an axial $L_{\mu-\tau}$ gauge boson has a prediction for a scalar particle in a mass range that can be probed by colliders?

2. What is the range of phenomenologically allowed $S$ mass including perturbativity limits on $\lambda$ and a motivated range of $m_{A^{\prime}}$ and $g_{X}$. For example: perhaps the authors imagine a range of $m_{A^{\prime}}$ below some benchmark mass where certain experimental constraints on $g_{X}$ become very strong. Then with that set of constraints (which should be stated clearly, see minor point #1 below), one may give a range of $m_S$ and comment on the experimental constraints.

3. Above (34): the authors "assume negligible Higgs-portal mixing." Is this interaction not generated at loop level? It seems that $S$-$h$ mixing cannot be avoided due to $\mu$ and $\tau$ loops. In turn, this seems like it would lead to strong experimental bounds on the UV completion. In fact, once there is mixing, is there not a resonance where the mixing becomes large as $m_{S}\rightarrow m_{h}$? It would be useful to quantify the size of this mixing over the allowed range of $m_{S}$. Existing Higgs measurements may set the strongest bounds on the UV completion. If these bounds are obviously negligible (though again, I expect this to be strongly constrained as $m_{S}\rightarrow m_{h}$), then the authors should present this as the justification for ignoring $m_{S}$ in the low-energy theory. (Though I am still skepticial that the $m_{S}$ can be ignored since it cannot formally decouple.)

### 2. Motivating the range of effective theory parameters

To further aid in the comparison between the UV theory and the two-parameter low-energy theory, it would be useful to explicitly state in one place (perhaps in a table or a figure like Fig. 2) the range of the effective model parameters that are feasible. The main phenomenological results are in Fig. 2, but it was not clear why this range of couplings and $A^{\prime}$ masses were chosen: are values outside this range not allowed? What, if anything, does the perturbativity of the UV theory impose on the effective parameters?

### 3. Are neutrino oscillations possible?

The Standard Model is defined with only left-handed neutrinos because of the possibility that neutrinos are their own antiparticle. In such a case neutrino masses are generated through, e.g. through the Weinberg operator.

1. In this model, $U_{A}(1)_{L_{\mu-\tau}}$ invariance allows Weinberg operators for each generation. However, it appears that both the Yukawa matrices and neutrino masses must be aligned and therefore a non-trivial PMNS matrix does not appear to be possible.

2. Perhaps a full model would require right-handed neutrinos. These would now be charged under $U_{A}(1)_{L_{\mu-\tau}}$, which likely means the second and third generation must appear as vectorlike combinations. However, it seems to me that mixing between generations is prohibited by $U_{A}(1)_{L_{\mu-\tau}}$.

Thus it is not obvious to me how neutrino oscillations can be included in this framework. If there is a simple solution, the authors should include it. If there is a known less-simple solution in the literature, the authors should cite this. Otherwise, at best this will be a confusing point. At worst, it would make the construction inconsistent with neutrino oscillation experiments.

### 4. Is this the full set of experimental constraints?

The second half of the manuscript presents a set of experimental bounds on the two-parameter effective $A^{\prime}$ model. It is not obvious if this is the full set of constraints on the model. (See also point #1 above: I would have liked to see a section discussing the bounds on the $S$ within this model since it cannot be decoupled.) The following experimental bounds seem like they could be relevant. It would be helpful to either include them or justify why they are subdominant to the experiments presented.

1. Neutrino oscillation observations. See point #3 above. It appears that this model predicts a unit PMNS matrix, which is inconsistent with neutrino oscillations.

2. There is no quantitative estimate of the amount of kinetic mixing generated with the 'benchmark' choices of $\theta \leq 10^{-2}$. The authors make the insightful point that kinetic mixing goes to zero in the axial limit, but because this limit is tied to the size of the mixing (the mass of the vectorlike leptons), for the above benchmark there is non-zero kinetic mixing. It would be useful to have parametric estimates of the amount of kinetic mixing one expects so that readers may compare to experimental bounds. One could invoke parametric expressions in the literature for the relevant loop diagrams.

3. Another way of reframing the above point: the bounds presented are in the pure axial limit. Since the authors present a UV model that only realizes the axial coupling in a decoupling limit, it would be useful to comment on possible experimental bounds on the small vector-like coupling in a model with non-infinite vectorlike fermion masses. If these bounds are always small compared to the axial bounds, this should be stated and justified. The importance of this point is as follows: often bounds are sensitive to the chiral structure of interactions. Sometimes a vector interaction is more tightly constrained than its axial counterpart. Since the authors focus on the phenomenology in the axial limit, one wants to make sure that any small-but-finite vector interaction isn't significant because the constraints on the coupling are orders-of-magnitude larger than the axial coupling.

4. Are stellar cooling bounds not relevant? See e.g. 2511.09619 for a recent paper on this. If they are not, then this is certainly worth justifying.

## Minor Points

The following points could be improved for clarity.

### 1. Range of parameters

The general cosntruction of the model is clearly written, but it is difficult for the reader to envision the mass and coupling range that the authors are targeting. It would be very helpful if the authors decide on a range of $m_{A^{\prime}}$ and $g_{X}$ of interest. For example: is there a range of masses where experimental or theoretical limits are less constraining? Is there some set of phenomenology that the authors week to realize with a "light" $A'$? If so, they should define "light." (see, e.g. the first word of the introduction, which is not defined with respect to any reference mass scale.)

### 2. Defining the pure-axial limit

Equation (12) gives the coupling of the $A^{\prime}$ to the mass-basis fields. It is here that the pure axial coupling limit is defined? i.e. $\theta_{\mu R}\rightarrow 0$? If that is the case, it would help to define this as the pure-axial limit, a phrase which is used below (36) but not otherwise quantified.

### 3. Bounds on the vectorlike leptons

Because the mixing angles scale inversely with the vectorlike lepton masses, it would be helpful to present lower limits on these masses. This, in turn, gives an upper limit on the $\theta_{(\mu,\tau)R}$ mixing angles which then gives an upper limit on the $A^{\prime}$ vectorlike coupling to $L_{\mu-\tau}$. How do these bounds compare with the $\theta_{(\mu,\tau)(L,R)}$ bounds in equation (27)?

### 4. Conservative benchmark

Equation (27) is presented as a "conservative benchmark." What does this mean? A benchmark point would be a choice of this mixing angles. A constraint is an upper bound. Eq. (27) is written as an upper bound, but is described as a benchmark. This is not simply semantic: readers would want to understand if $10^{-2}$ is an experimental upper limit or simply a convenient choice.

### 5. What is the purpose of including muon collider bounds?

The second half of the paper focuses on existing experimental bounds on the effective theory. It is a strange change in tone to include hypothetical muon collider bounds for future reach. The authors do not justify why a future muon collider is the way to test this model in the future and the section feels like it is tacked on. Most of the section emphasizes that the muon collider search would be a 'standard' follow up of existing work (Ref 83) and so this section does not seem particularly novel. The authors simply focus on the forward-backward asymmetry. Why not also include polarization asymmetries? Or would there be asymmetries in the $ee$ versus $\tau\tau$ final states? Given the first half of the paper, though, it seems that the real 'smoking gun' for this UV completion is the physics of the $S$ particle which should be tested in any Higgs-factory phase of a future lepton collider. I feel that this section either adds too little and should be downplayed as an example of future tests, or otherwise should have its own full fledged exploration (which may be a separate paper).

### 6. Terminology

1. The word "light" on page 2 has no reference scale.
2. At the bottom of page 11, when referring to Table II, the authors write "representative bounds." What does representative mean? Does it mean these are the most stringent bounds? Are these "some" bounds? Is the list 'complete' in any sense?
3. Between page 12–13: "...do not provide a universal $g_{X}$ bound, but they show that the intermediate scalar-mass region cannot simply be assumed unconstrained." What does intermediate mass mean? It is also not clear what the intended content of this statement is: are the authors presenting a bound? Why would the reader assume that a new particle in this range would be unconstrained?
4. Below (34): "we impose Eq. (34) point by point", it's not clear what is meant by 'point.'
5. Page 21, first paragraph of Section E. What is the "parameter region of interest"? This wasn't clearly defined anywhere.
6. Page 21, end of section D: What's the significance of the $v_{S}=2$ GeV line? What does it mean that $y_{s\mu\mu}$ "becomes large" (nonperturbative)? Why plot it? Is it a perturbativity bound?

## Recommendation

In its current form, the paper is not ready for publication. The major points above must be addressed. It's entirely possible that I have misinterpreted some of these points, but if that is the case then they at least indicate ideas that must be clarified before the manuscript merits publication. I strongly encourage the authors to further address the minor points.

The paper can be a useful addition to the model building literature. However, the question of whether this class of model can be consistent with neutrino oscillations is critical. I also feel that dismissing the physics of the scalar $S$ ignores the actual predictions of the UV model—otherwise the authors are simply justifying the phenomenology of the effective axial theory.

## Statement

No artificial intelligence tools were used in the preparation of this review. (All mistakes are human generated.)
