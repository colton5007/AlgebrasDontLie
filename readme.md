# Algebras Don't Lie!
## Inspiration
Throughout my research experience in mathematics I have seen countless mathematicians plagued with horrible non-geometric intuition when it comes to working with Lie Algebras and Lie Groups. Despite their often beautiful symmetries and powerful realizations from fundamental linear transformations, they can be unnerving to work with and require a lot of grunt work to get an intuition about a particular Lie Algebra. Algebras Don't Lie! serves to bridge the gap between the powerful computational methods that have been developed to calculate these properties and the general lack of computer aptitude often found among many pure mathematicians and physicists. By taking advantage of these methods we can hasten research and allow for more intuitive teachings of these algebras.

## What It Does

Algebras Don't Lie! calculates and plots many nice properties of low-dimensional cartan-typed Lie Algebras. To be as inclusive as possible, we have included the standard $A_n, B_n, C_n, D_n$ cartan types as well as the more exotic $E_6,E_7, E_8, F_4$ and $G_2$ cartan types. While not everything can be calculated in these exotic cases, we can certainly gain intuition about the ambient space and even the Dynkin diagrams can be useful. In addition to the basic cartan types, within reason we can consider affine Lie algebras and tensor products provided they sensibly are a cartan type as well. We can realize root polytopes and plot them along with projections for higher dimensional polytopes that are not immediately visualized in $\mathbb{R}^2$ or $\mathbb{R}^3$. Included in these calculations and plots are the hyperplanes through these roots (orthogonal when simple and generally not in the case of co-roots which can be clearly seen). This is a nice way of presenting these root systems in an ambient space and provides a lot of structure and symmetry of the Lie algebra. Furthermore, we can visualize hedron polytope embeddings from 4 and 5 dimensional Lie algebra root systems into $\mathbb{R}^3$, a strikingly beautiful, yet useful visualization. Additionally, we have included the Dunkin Diagrams, Coxeter numbers (and dual), and the Coxeter Matrix for these cartan-types which should be quite easily computable and thus will calculate for nearly any finite-dimensional Lie algebra. Finally, due to the close relationship between the Lie algebra, its tangent group, and the Weyl group, we have added the Cayley Graph of the Weyl group embedded in $\mathbb{R}^3$ to see some of these beautiful symmetries.

## How We Built It

We built this primarily using Sage and SageCell which provided a large brunt of the calculations and formulations that we were able to present along with their impeccable plotting library that makes for lovely interactive plots. In addition we incorporated a web server to allow for easy distribution and presentation for researchers and hobbyist alike.

## Challenges We Ran Into

I have not had an opportunity to mess with the Lie theory side of Sage before. It posed many of its own unique challenges with a slightly convoluted programming scheme making things a tad bit more difficult too. In addition, SageCell (from what I know now) is not well built for these types of high-compute projects and not having enough time to host my own SageCell server hindered performance greatly.

## Accomplishments

There is a certain amount of beauty that can be achieved from such a lovely formulation of these Lie algebras, We can better understand math by first better visualizing it. The importance of having a utility now to help with this often heavily diagramatic field cannot be overstated and it is incredibly satisfying to have such a utility. 

## What We Learned

1. It's really tiring to work with math at 5am.
2. Sage is really powerful.
3. Lie algebra polytopes are gorgeous.

## Next Steps
There are a few directions I'd like to continue this project. First and foremost, the ability to calculate the projection onto the Coexeter plane for a general Lie algebra would be incredible for visualizing symmetries of higher-dimensional Lie algebras (including the highly symmetric $E_8$ algebra that exists as a $248$ dimensional vector space.) These would be incredibly helpful for mathematics reasearch. In addition, being able to provide more general means of a user to apply a projection based off the structure of the algebra would be great. Currently our biggest bottleneck in many of the visualizations are due to the dimensions of the Lie algebras. If we can create strong methods for these types of projections, we can hope to better understand these complicated structures.# AlgebrasDontLie
