# draft-ietf-netconf-restconf

This repository is for the development of a IETF draft for the [NETCONF working group](http://datatracker.ietf.org/wg/netconf/charter/).

## Links

* IETF Page: https://tools.ietf.org/html/draft-ietf-netconf-restconf
* Mailing List: https://www.ietf.org/mailman/listinfo/netconf
* Issue Tracking: https://github.com/netconf-wg/restconf/issues


## Issue States

The following labels are used in the issue tracker for issues
in the "open" state:

- NEW:  A submitted issue
- OPEN: An accepted issue open to discussion
- DEAD: A rejected issue closed to discussion
- VERIFY: An open issue with a solution proposal that needs to be verified on the mailing list
- EDIT: The issue is waiting for the document editor(s) to make the corresponding changes
- REVIEW: The edits have been done and the updated I-D need to be reviewed
- DONE: The edits have been reviewed and the issue has been resolved


## pyang

This draft contains examples using YANG 1.1.
You can get the version of pyang that supports YANG 1.1 from github.

     git clone http://github.com/mbj4668/pyang
     cd pyang
     git checkout yang-1.1
     sudo python setup.py install

## Contributing

Before submitting feedback, please familiarize yourself with our current issues
list and review the [working group home page](http://datatracker.ietf.org/wg/netconf/charter/). If you're new to this, you may also want to read the [Tao of the
IETF](https://www.ietf.org/tao.html).

Be aware that all contributions to the specification fall under the "NOTE WELL"
terms outlined below.

1. The best way to provide feedback (editorial or design) and ask questions is
sending an e-mail to [our mailing list](https://www.ietf.org/mailman/listinfo/netconf). This will ensure that the entire Working Group sees your input in a timely fashion.

2. If you have **editorial** suggestions (i.e., those that do not change the
meaning of the specification), you can either:

  a) Fork this repository and submit a pull request; this is the lowest
  friction way to get editorial changes in.
  
  b) Submit a new issue to Github, and mention that you believe it is editorial
  in the issue body. It is not necessary to notify the mailing list for
  editorial issues.
  
  c) Make comments on individual commits in Github. Note that this feedback is
  processed only with best effort by the editors, so it should only be used for
  quick editorial suggestions or questions.

3. For non-editorial (i.e., **design**) issues, you can also create an issue on
Github. However, you **must notify the mailing list** when creating such issues,
providing a link to the issue in the message body.

  Note that **github issues are not for substantial discussions**; the only
  appropriate place to discuss design issues is on the mailing list itself.


## NOTE WELL

Any submission to the [IETF](https://www.ietf.org/) intended by the Contributor
for publication as all or part of an IETF Internet-Draft or RFC and any
statement made within the context of an IETF activity is considered an "IETF
Contribution". Such statements include oral statements in IETF sessions, as
well as written and electronic communications made at any time or place, which
are addressed to:

 * The IETF plenary session
 * The IESG, or any member thereof on behalf of the IESG
 * Any IETF mailing list, including the IETF list itself, any working group 
   or design team list, or any other list functioning under IETF auspices
 * Any IETF working group or portion thereof
 * Any Birds of a Feather (BOF) session
 * The IAB or any member thereof on behalf of the IAB
 * The RFC Editor or the Internet-Drafts function
 * All IETF Contributions are subject to the rules of 
   [RFC 5378](https://tools.ietf.org/html/rfc5378) and 
   [RFC 3979](https://tools.ietf.org/html/rfc3979) 
   (updated by [RFC 4879](https://tools.ietf.org/html/rfc4879)).

Statements made outside of an IETF session, mailing list or other function,
that are clearly not intended to be input to an IETF activity, group or
function, are not IETF Contributions in the context of this notice.

Please consult [RFC 5378](https://tools.ietf.org/html/rfc5378) and [RFC 
3979](https://tools.ietf.org/html/rfc3979) for details.

A participant in any IETF activity is deemed to accept all IETF rules of
process, as documented in Best Current Practices RFCs and IESG Statements.

A participant in any IETF activity acknowledges that written, audio and video
records of meetings may be made and may be available to the public.
